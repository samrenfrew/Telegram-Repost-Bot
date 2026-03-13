import textwrap

from repostbot.db.db import connect_db


def init_db_tables():
    with connect_db() as connection:
        cursor = connection.cursor()
        table_sql = [
            _init_reposts_db_sql(),
            _init_hash_whitelist_db_sql(),
            _init_deleted_messages_table_sql()
        ]
        cursor.executescript("\n\n".join(table_sql))


def _init_reposts_db_sql():
    return textwrap.dedent("""
        create table if not exists reposts(
            id                INTEGER not null primary key autoincrement,
            group_id          INTEGER not null,
            user_id           INTEGER,
            message_id        INTEGER not null,
            hash_value        TEXT not null,
            hash_checked_date DATE
        );

        create index if not exists reposts_group_id_index
            on reposts (group_id);

        create unique index if not exists reposts_group_id_message_id_hash_value_unique_index
            on reposts (group_id, message_id, hash_value);
    """)


def _init_hash_whitelist_db_sql():
    return textwrap.dedent("""
        create table if not exists hash_whitelist(
            id         INTEGER not null primary key autoincrement,
            group_id   INTEGER not null,
            hash_value TEXT not null
        );

        create index if not exists hash_whitelist_group_id_index
            on hash_whitelist (group_id);

        create unique index if not exists hash_whitelist_group_id_hash_value_unique_index
            on hash_whitelist (group_id, hash_value);
    """)


def _init_deleted_messages_table_sql():
    return textwrap.dedent("""
        create table if not exists deleted_messages(
            id         INTEGER not null primary key autoincrement,
            group_id   INTEGER not null,
            message_id INTEGER not null
        );

        create index if not exists deleted_messages_group_id_index
            on deleted_messages (group_id);

        create unique index if not exists deleted_messages_group_id_message_id_unique_index
            on deleted_messages (group_id, message_id);
    """)


if __name__ == '__main__':
    init_db_tables()
