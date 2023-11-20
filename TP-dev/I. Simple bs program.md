# I. Simple bs program

## 1. First steps


🌞 **`bs_server_I1.py`**

[bs_server_I1.py](bs_python_I1.py)

```
[uliaxe@server TP-dev]$ python bs_server_I1.py
Connected by ('10.1.2.11', 54320)
Données reçues du client : b'Meooooo !'
```


🌞 **`bs_client_I1.py`**

[bs_client_I1.py](bs_client_I1.py)

```
[uliaxe@client TP-dev]$ python bs_client_I1.py
Received b'Hi mate.'
```

🌞 **Commandes...**

dnf install python git

sudo firewall-cmd --add-port=13337/tcp --permanent

sudo firewall-cmd --reload

sudo ss -tnlp | grep 13337

## 2. User friendly
🌞 **`bs_client_I2.py `**
[bs_client_I2.py](bs_client_I2.py)

🌞 **`bs_server_I2.py`**
[bs_server_I2.py](bs_server_I2.py)

## 3. You say client I hear control

🌞 **`bs_client_I3.py`**

[bs_client_I3.py](bs_client_I3.py)