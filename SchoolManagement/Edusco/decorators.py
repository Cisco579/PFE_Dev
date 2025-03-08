# from django.contrib.auth.decorators import user_passes_test

# def admin_required(view_func):
#     decorated_view_func = user_passes_test(lambda u: u.is_authenticated and u.role == 'admin', login_url='account_login')(view_func)
#     return decorated_view_func

# def student_required(view_func):
#     decorated_view_func = user_passes_test(lambda u: u.is_authenticated and u.role == 'student', login_url='account_login')(view_func)
#     return decorated_view_func

# def teacher_required(view_func):
#     decorated_view_func = user_passes_test(lambda u: u.is_authenticated and u.role == 'teacher', login_url='account_login')(view_func)
#     return decorated_view_func