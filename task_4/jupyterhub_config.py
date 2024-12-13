# Используем DummyAuthenticator
c.JupyterHub.authenticator_class = 'dummy'

# Разрешаем всем пользователям входить
c.DummyAuthenticator.allow_all = True

# Устанавливаем администратора
c.JupyterHub.admin_users = {'admin'}

# Разрешаем создание системных пользователей
c.LocalAuthenticator.create_system_users = True

# Устанавливаем рабочую директорию для Jupyter Notebook
c.Spawner.notebook_dir = '/home/jovyan/all_notebooks'

# Устанавливаем spawner
c.JupyterHub.spawner_class = 'jupyterhub.spawner.SimpleLocalProcessSpawner'

