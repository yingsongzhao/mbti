"""数据库模型 — SQLite + 原生 SQL"""

import sqlite3
import os

DB_DIR = os.path.join(os.path.dirname(__file__), "data")
DB_PATH = os.path.join(DB_DIR, "mbti.db")


def get_db():
    """获取数据库连接（自动创建目录和表）"""
    os.makedirs(DB_DIR, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    return conn


def init_db():
    """初始化数据库表"""
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS results (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            candidate   TEXT DEFAULT '匿名',
            e_score     INTEGER NOT NULL,
            i_score     INTEGER NOT NULL,
            n_score     INTEGER NOT NULL,
            s_score     INTEGER NOT NULL,
            f_score     INTEGER NOT NULL,
            t_score     INTEGER NOT NULL,
            j_score     INTEGER NOT NULL,
            p_score     INTEGER NOT NULL,
            mbti_type   TEXT NOT NULL,
            created_at  TEXT NOT NULL DEFAULT (datetime('now', 'localtime'))
        )
    """)
    conn.commit()
    conn.close()


def save_result(candidate: str, scores: dict) -> int:
    """保存一份测试结果，返回 ID"""
    conn = get_db()
    cur = conn.execute(
        """INSERT INTO results
           (candidate, e_score, i_score, n_score, s_score,
            f_score, t_score, j_score, p_score, mbti_type)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        (
            candidate or "匿名",
            scores["e_score"], scores["i_score"],
            scores["n_score"], scores["s_score"],
            scores["f_score"], scores["t_score"],
            scores["j_score"], scores["p_score"],
            scores["mbti_type"],
        ),
    )
    conn.commit()
    row_id = cur.lastrowid
    conn.close()
    return row_id


def get_all_results():
    """获取所有测试结果（按时间倒序）"""
    conn = get_db()
    rows = conn.execute(
        "SELECT * FROM results ORDER BY created_at DESC"
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def get_type_distribution():
    """获取 16 型人格分布统计"""
    conn = get_db()
    rows = conn.execute(
        """SELECT mbti_type, COUNT(*) as count
           FROM results
           GROUP BY mbti_type
           ORDER BY count DESC"""
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def get_dimension_stats():
    """获取各维度平均分统计"""
    conn = get_db()
    row = conn.execute(
        """SELECT
             COUNT(*) as total,
             AVG(e_score) as avg_e, AVG(i_score) as avg_i,
             AVG(n_score) as avg_n, AVG(s_score) as avg_s,
             AVG(f_score) as avg_f, AVG(t_score) as avg_t,
             AVG(j_score) as avg_j, AVG(p_score) as avg_p
           FROM results"""
    ).fetchone()
    conn.close()
    return dict(row) if row and row["total"] else None
