import os
import chalk

print(f"Je suis exécuté depuis : {chalk.blue(os.getcwd())}")
print(f"et je suis : {chalk.blue(__file__)}")
