import os
from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/')

def programa ():
    def primo (n):
        if n != 0 and n !=1:
            if n>3:
                for i in range(2,n):
                    if n %i==0:
                        return False
            return True
        return


    i=1
    s=''
    cont =0
    while True:
        primo(i)
        i+=1
        
        if cont == 100:
            break
        if primo(i) == True:
            cont+=1
            s+=str(i) + ', '
            
    return (s [0:len(s)-2])

    print(programa())
            
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    