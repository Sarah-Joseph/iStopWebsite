import django_tables2 as tables


class Table(tables.Table):
    Meta:
        attrs = {
            'th' : {
                '_ordering': {
                    'orderable': 'sortable',
                    'ascending': 'ascend',
                    'descending': 'descend'
                }
             }
        }

	 
