# grpc-python-example
________________________________________________________________________________________

Example of a Python API using gRPC...

Create and activate the virtual environment...
```
virtualenv --python=python3.8 .venv
source .venv/bin/activate
```

Install dependencies...
```
pip install --upgrade pip
pip install -r requirements.txt
```

Compile the .proto files...
```
python -m grpc_tools.protoc -I definitions/ --python_out=definitions/builds/ --grpc_python_out=definitions/builds/ definitions/service.proto
```

Start the servers...
```
python server.py 
python flask_server.py
python fastapi_server.py
```

Results...
```
FastAPI                 Flask                   gRPC
2.5365726947784424      3.588320016860962       0.6878361701965332
2.4663445949554443      3.4863481521606445      0.7431104183197021
2.8214125633239746      3.522181749343872       0.719865083694458
```
