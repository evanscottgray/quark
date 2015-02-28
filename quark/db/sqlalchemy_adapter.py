from sqlalchemy.orm.persistence import BulkUpdate
from sqlalchemy import sql


class BulkUpdateMySqlLimit(BulkUpdate):
    def __init__(self, query, values, **kwargs):
        super(BulkUpdateMySqlLimit, self).__init__(query, values)
        self.kwargs = kwargs

    def _do_exec(self):
        update_stmt = sql.update(self.primary_table,
                                 whereclause=self.context.whereclause,
                                 values=self.values,
                                 **self.kwargs)
        self.result = self.query.session.execute(
            update_stmt, params=self.query._params)
        self.rowcount = self.result.rowcount


def update_limit(query, values, limit):
    update_op = BulkUpdateMySqlLimit(query, values, mysql_limit=limit)
    update_op.exec_()
    return update_op.rowcount
