# Configuration settings for the project

DATABASE = {
    'name': 'database_name',
    'user': 'database_user',
    'password': 'database_password',
    'host': 'localhost',
    'port': 5432
}

DIRECTORIES = {
    'data_directory': '/path/to/data',
    'log_directory': '/path/to/logs',
    'temp_directory': '/path/to/temp'
}

SCRAPER = {
    'url': 'http://example.com',
    'user_agent': 'Mozilla/5.0',
    'timeout': 10
}

ANALYZER = {
    'analysis_type': 'default',
    'output_directory': '/path/to/output',
}

VISUALIZER = {
    'chart_type': 'bar',
    'output_format': 'png',
}

SEARCH = {
    'search_engine': 'google',
    'max_results': 100
}