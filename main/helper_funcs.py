def _validate_date(date: str) -> str:
    '''Used in _format_date to return validation keys.'''
    try:
        int(date)
    except ValueError:
        return 'NotIntegerError'
    if len(date) != 6:
        return 'LengthError'
    elif not 1 <= int(date[:2]) <= 31:
        # Does not check wether day makes sense according
        # to the current month
        return 'DayError'
    elif not 1 <= int(date[2:4]) <= 12:
        return 'MonthError'
    else:
        return 'Valid'

def _format_date(date: str) -> str:
    '''
    Formats dates in the form of ``ddmmyy`` into ``Month dd, 20yy``.

    For example, ``date='010101'`` returns ``'January 1, 2001'``.
    '''
    if (validation_key := _validate_date(date)) != 'Valid':
        return validation_key
    
    month_dict = {
        '01': 'January',
        '02': 'February',
        '03': 'March',
        '04': 'April',
        '05': 'May',
        '06': 'June',
        '07': 'July',
        '08': 'August',
        '09': 'September',
        '10': 'October',
        '11': 'November',
        '12': 'December'
    }
    date_list = []
    for i in range(0, len(date)-1, 2):
        date_list.append(date[i:i+2])
    day, month, year = date_list
    if day[0] == '0':
        day = day[-1]
    month = month_dict[month]
    formatted_date = '{} {}, 20{}'.format(month, day, year)
    return formatted_date

def get_project_list() -> list[tuple[str]]:
    '''
    Obtain a ``list`` containing ``tuples`` of projects from the
    project-data.txt file.
    
    The ``tuples`` include the project's name, upload date,
    and completion completed as ``strings``.
    '''
    proj_list: list[tuple[str]] = []
    try:
        with open('project-data.txt') as file:
            for line in file:
                if '//' in line:
                    continue
                name, upload, completed = line.split()
                project = name.replace('-', ' ').capitalize(), _format_date(upload), completed
                proj_list.append(project)
    except Exception