import datetime
def decorator_v2(log_path):
    def decorator(some_function):
        def loger(*args, **kwargs):
            log = {}
            date = datetime.datetime.today()
            log["date_time"] = date.strftime('%d-%m-%Y %H:%M')
            log["name_of_function"] = some_function.__name__
            log["arguments"] = f'{args}{kwargs}'
            log["result"] = some_function(*args, **kwargs)
            with open(f'{log_path}log.txt', 'a') as f:
                f.write(f'{log}\n')
            result = some_function(*args, **kwargs)
            return result
        return loger
    return decorator

