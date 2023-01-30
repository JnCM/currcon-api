from environs import Env


env = Env()
env.read_env(".env", recurse=False)

API_KEY = env.str("API_KEY")
BASE_URL = env.str("BASE_URL")