import subprocess

def git_auto_push(commit_message: str):
    try:
        
        subprocess.run(['git', 'add', '.'], check=True)

        if not commit_message :
            raise Exception()
        
        subprocess.run(['git', 'commit', '-m', commit_message], check=True)

        subprocess.run(['git', 'push'], check=True)

        print('깃 푸시 성공!!!')
    
    except subprocess.CalledProcessError as e:
        print(f"깃 푸시 실패!!! : {e}")

if __name__ == '__main__':
    git_auto_push('commit completed')