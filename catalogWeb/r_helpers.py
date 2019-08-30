from functools import wraps


# def add_tab_name(tab_name):
#     def real_decorator(function):
#         def wrapper(*args, **kwargs):
#             # Call the base implementation first to get a context
#             context = super().get_context_data(**kwargs)
#             # Add in a QuerySet of all the books
#             context['tab_name'] = tab_name
#             return context
#         return wrapper
#     return real_decorator

def add_tab_name(tab_name):
    def real_decorator(func):
        def wrapper(*args, **kwargs):
            # Call the base implementation first to get a context
            context = func(*args, **kwargs)
            # Add in a QuerySet of all the books
            context['tab_name'] = tab_name
            return context
        return wrapper
    return real_decorator

