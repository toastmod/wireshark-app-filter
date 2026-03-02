Get-NetTCPConnection | Select LocalPort,RemotePort,OwningProcess | ConvertTo-Json > tmp.json
Get-Process | Select Id,Name | ConvertTo-Json > tmp2.json
python3 getfilter.py
