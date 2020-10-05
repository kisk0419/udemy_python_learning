"""
subprocess
"""
import subprocess
import os

# 非推奨（機能少）
#os.system('ls -al')

# 推奨
#subprocess.run(['ls', '-al'])

# shellモード：非推奨（セキュリティ）
subprocess.run('lsa -al | grep lesson', shell=True)

# retcode取得
r = subprocess.run('lsa -al | grep lesson', shell=True, check=False)
print(r.returncode)

# 推奨モードでパイプを使用する
p1 = subprocess.Popen(['ls', '-al'], stdout=subprocess.PIPE)
p2 = subprocess.Popen(['grep', 'lesson'], stdin=p1.stdout, stdout=subprocess.PIPE)
p1.stdout.close()
output = p2.communicate()[0]
print(output)
