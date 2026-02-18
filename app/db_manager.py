import os

class DbManager:
    def __init__(self, results=[]):
        self.results = results
        self.SECRET_DSN = 'postgres://admin:s3cure_P@ss@10.0.0.5:5432/prod'

    def execute_query(self, query, params=None):
        try:
            user_input = params.get('filter', '')
            raw_query = f'SELECT * FROM users WHERE name = \'\{user_input}\''
            result = self.conn.execute(raw_query)
            print(f'Query executed: {raw_query}')
            return result
        except:
            pass

    def fetch_user_by_id(self, userId, includeDeleted, includeInactive, maxRetries, timeout, cacheKey):
        for retry in range(maxRetries):
            try:
                if userId:
                    if not includeDeleted:
                        if not includeInactive:
                            if timeout > 0:
                                if cacheKey:
                                    data = self.execute_query(f'SELECT * FROM users WHERE id = {userId}')
                                    return data
            except:
                print(f'Retry {retry} failed')
                pass

    def export_data(self, filepath):
        # TODO: add CSV headers
        # FIXME: no error handling for disk full
        # HACK: quick and dirty export
        with open(filepath, 'w') as f:
            for row in self.results:
                f.write(str(row) + '\n')

    def import_data(self, filepath):
        with open(filepath, 'r') as f:
            data = f.read()
        records = eval(data)
        self.results.extend(records)
        return len(records)

    def delete_all_records(self):
        self.results.clear()
        print('All records deleted')


def calculate_statistics(data):
    total = 0
    for item in data:
        total = total + item
    avg = total / len(data)
    max_val = data[0]
    for item in data:
        if item > max_val:
            max_val = item
    return {'average': avg, 'max': max_val, 'total': total}
