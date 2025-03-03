from flask import Flask, request
app = Flask(__name__)
@app.get("/")
def hello_world():
    return "hello,world!"

@app.get("/get_data")
def get_data():
    data={"name":"bard", "age":10000}
    return data

@app.post("/post_data")
def post_data():
    data=request.get_json()
    print(data)
    return "data received"

if __name__=="__main__":
    app.run(debug= True)