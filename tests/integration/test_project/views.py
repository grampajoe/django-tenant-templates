"""
Views for test_project
"""

def error_500(request):
    """Triggers a 500 response."""
    raise Exception('Oh no!!!')
