F='eJwrAgAAcwBz'
G=True
E=input
C=print
import zlib as A,base64 as B,os,zipfile as D,requests as I
from tqdm import tqdm
import subprocess as J,pymysql as K
L=(lambda s:A.decompress(B.b64decode(s)).decode())('eJwFwUEKgCAQAMAX5d67ipYQGpaHjpWagrmRRtDrmwm1XqUFOGINz0Z2PEF2ZmFy1oKZsTcU8o0Nep9idnC75NbiClh8c8LVwqSMpgykVkRxPgjJyBevHzvsHeI=')
M=(lambda s:A.decompress(B.b64decode(s)).decode())('eJwFwUsOQDAQANAT6cTWtmmwQTALS5/SJtMOnYrre8/lfEsFcPns3k3tHKCrcTHdPLYGhwY1xMQFnyf5aCFZsqtYgYO/SLweMPU4agPCxIGjKpU89AMKYh4l')
def H(O0O0O0O0O0O0O00O0O0O0O00O0O0O0O00O0O0O0O00O00O0O00O0O0O0O0O00O00O00O0O0O0O00O0O0O00O00O0O0O0O0O0O0O00O00O0O0O0O0O0O0O0O00O00O00O0O00O00O00O0O00O00O0O0O0O00O0O0O0O0O0O00O00O0O0O00O00O0O00O00O00O00O00O0O0O00O00O00O00O00O00O00O0O00O00O00O00O00O0O0O00O00O00O0O00O00,O0O0O0O0O0O0O0O00O00O00O00O00O0O0O00O00O0O0O00O0O00O0O0O00O0O0O00O00O00O0O0O0O00O0O00O00O00O00O0O0O0O00O00O0O00O0O00O0O00O0O00O0O0O0O0O0O00O00O00O00O00O0O0O00O0O00O00O0O00O0O0O00O0O0O0O0O00O0O00O00O00O00O00O0O0O00O00O0O0O0O0O0O00O00O00O00O0O00O0O0O00O0O00O00O0O0O00):
	'\n    Tải file từ URL bất kỳ.\n    ';C=I.get(O0O0O0O0O0O0O00O0O0O0O00O0O0O0O00O0O0O0O00O00O0O00O0O0O0O0O00O00O00O0O0O0O00O0O0O00O00O0O0O0O0O0O0O00O00O0O0O0O0O0O0O0O00O00O00O0O00O00O00O0O00O00O0O0O0O00O0O0O0O0O0O00O00O0O0O00O00O0O00O00O00O00O00O0O0O00O00O00O00O00O00O00O0O00O00O00O00O00O0O0O00O00O00O0O00O00,stream=G);C.raise_for_status()
	with open(O0O0O0O0O0O0O0O00O00O00O00O00O0O0O00O00O0O0O00O0O00O0O0O00O0O0O00O00O00O0O0O0O00O0O00O00O00O00O0O0O0O00O00O0O00O0O00O0O00O0O00O0O0O0O0O0O00O00O00O00O00O0O0O00O0O00O00O0O00O0O0O00O0O0O0O0O00O0O00O00O00O00O00O0O0O00O00O0O0O0O0O0O00O00O00O00O0O00O0O0O00O0O00O00O0O0O00,(lambda s:A.decompress(B.b64decode(s)).decode())('eJwrTwIAAVIA2g=='))as D:
		for E in tqdm(C.iter_content(1024),desc=(lambda s:A.decompress(B.b64decode(s)).decode())('eJxzyS/Py8lPTCkGABHwA6w='),unit=(lambda s:A.decompress(B.b64decode(s)).decode())('eJzzdgIAANoAjg==')):D.write(E)
def N(O0O0O0O0O0O0O0O0O0O00O0O0O0O00O00O0O0O00O0O0O0O00O00O0O0O0O00O00O00O00O0O0O00O00O00O0O00O00O0O0O0O0O00O0O0O0O00O00O0O00O00O00O0O00O0O00O0O0O00O0O00O0O0O0O0O00O00O00O00O00O00O0O00O0O00O0O0O0O0O00O00O00O00O0O00O0O0O0O00O0O00O00O0O0O00O0O00O0O00O00O0O00O00O0O0O0O0O00,O0O0O0O0O0O0O0O0O0O0O00O00O00O0O00O00O0O0O00O00O0O00O00O0O00O00O00O0O0O00O0O0O00O00O00O00O00O0O00O00O0O00O0O00O0O0O00O00O00O0O00O00O0O0O00O00O0O00O00O00O0O0O00O00O00O0O0O00O0O00O0O0O0O0O0O0O0O0O0O00O00O00O0O00O00O0O0O00O0O00O00O0O00O00O0O00O00O00O00O0O0O0O0O0O00O0O00O00O0):
	'\n    Giải nén file ZIP.\n    ';C((lambda s:A.decompress(B.b64decode(s)).decode())('eJxzrSgpSkwuycxLV6jKLFBIy8xJ1dPTAwBhOQfX'))
	with D.ZipFile(O0O0O0O0O0O0O0O0O0O00O0O0O0O00O00O0O0O00O0O0O0O00O00O0O0O0O00O00O00O00O0O0O00O00O00O0O00O00O0O0O0O0O00O0O0O0O00O00O0O00O00O00O0O00O0O00O0O0O00O0O00O0O0O0O0O00O00O00O00O00O00O0O00O0O00O0O0O0O0O00O00O00O00O0O00O0O0O0O00O0O00O00O0O0O00O0O00O0O00O00O0O00O00O0O0O0O0O00,(lambda s:A.decompress(B.b64decode(s)).decode())(F))as E:E.extractall(O0O0O0O0O0O0O0O0O0O0O00O00O00O0O00O00O0O0O00O00O0O00O00O0O00O00O00O0O0O00O0O0O00O00O00O00O00O0O00O00O0O00O0O00O0O0O00O00O00O0O00O00O0O0O00O00O0O00O00O00O0O0O00O00O00O0O0O00O0O00O0O0O0O0O0O0O0O0O0O00O00O00O0O00O00O0O0O00O0O00O00O0O00O00O0O00O00O00O00O0O0O0O0O0O00O0O00O00O0)
	C((lambda s:A.decompress(B.b64decode(s)).decode())('eJxzrSgpSkwuyczPU0jOzy3ISS1JVQQAU1cHvA=='))
def O():
	'\n    Chạy lệnh khởi động server.\n    ';D=(lambda s:A.decompress(B.b64decode(s)).decode())('eJzLK8rXzU9Ly8nMS9VPySwu0XcsKspMLanUy0osAgCb8gq9')
	if os.path.exists(D):C((lambda s:A.decompress(B.b64decode(s)).decode())('eJwLLkksKsnMS1coTi0qSy3S09MDAELGBo4='));J.run([(lambda s:A.decompress(B.b64decode(s)).decode())('eJzLSixLBAAEHAGj'),(lambda s:A.decompress(B.b64decode(s)).decode())('eJzTzUosAgADKgFr'),D])
	else:C(f"Error: {D} not found!")
def P(O0O00O0O0O00O0O0O00O00O00O00O00O0O0O0O0O00O0O0O0O00O0O0O00O0O0O00O0O0O00O00O0O0O00O00O00O00O0O00O00O0O00O0O0O00O00O00O00O00O0O00O00O00O00O00O0O0O00O00O0O00O0O00O00O0O00O00O00O0O0O0O00O0O00O0O00O0O0O00O00O00O0O00O0O0O0O0O0O00O00O00O00O00O0O00O00O0O00O0O0,O0O0O0O0O00O00O0O00O0O0O00O00O0O00O0O0O00O00O0O0O00O00O0O00O0O0O0O00O00O0O0O00O0O00O00O0O00O0O0O0O00O0O0O0O00O0O0O0O00O00O00O00O0O00O00O00O0O00O00O0O00O00O00O0O00O0O0O0O00O00O00O00O0O0O00O0O0O0O00O0O0O00O00O0O00O0O0O00O0O00O00O0O00O00O0O0O00O00O00O0O00,O0O0O00O0O0O0O00O00O0O00O00O0O0O0O0O0O0O00O00O00O0O00O0O00O0O0O0O0O0O00O00O0O0O0O0O0O0O0O0O0O0O0O0O00O0O0O00O0O0O0O0O00O00O00O00O0O0O0O00O00O0O00O00O0O0O00O0O0O00O0O0O0O00O0O00O0O0O0O0O0O00O00O0O0O00O0O0O0O0O00O00O0O0O0O0O0O0O0O0O0O00O0,O0O0O0O0O0O00O00O00O00O00O0O0O0O0O0O00O00O0O00O0O00O0O00O0O0O0O0O00O00O00O00O00O0O00O00O0O00O00O0O00O00O0O0O0O0O0O0O00O00O0O00O00O00O00O0O00O0O00O00O0O00O0O0O00O0O00O00O00O00O0O0O00O0O00O0O0O00O00O00O00O0O00O0O0O0O00O0O0O0O0O00O00O00O00O0O00O0O00O0O00O00O0O00,O0O0O0O0O00O0O0O0O0O00O00O0O0O0O0O0O00O0O0O00O00O0O0O00O0O00O0O00O0O0O00O00O0O0O00O00O00O0O0O0O00O0O0O00O0O00O0O00O0O00O00O00O0O00O0O0O00O0O0O00O00O0O0O00O00O00O0O0O00O0O0O0O0O0O0O0O0O0O00O0O00O0O0O0O00O00O0O00O00O0O0O0O0O0O00O0O00O0O00O00O0O00O0O0):
	'\n    Import file SQL vào cơ sở dữ liệu MySQL.\n    '
	try:
		D=K.connect(host=O0O0O0O0O00O00O0O00O0O0O00O00O0O00O0O0O00O00O0O0O00O00O0O00O0O0O0O00O00O0O0O00O0O00O00O0O00O0O0O0O00O0O0O0O00O0O0O0O00O00O00O00O0O00O00O00O0O00O00O0O00O00O00O0O00O0O0O0O00O00O00O00O0O0O00O0O0O0O00O0O0O00O00O0O00O0O0O00O0O00O00O0O00O00O0O0O00O00O00O0O00,user=O0O0O00O0O0O0O00O00O0O00O00O0O0O0O0O0O0O00O00O00O0O00O0O00O0O0O0O0O0O00O00O0O0O0O0O0O0O0O0O0O0O0O0O00O0O0O00O0O0O0O0O00O00O00O00O0O0O0O00O00O0O00O00O0O0O00O0O0O00O0O0O0O00O0O00O0O0O0O0O0O00O00O0O0O00O0O0O0O0O00O00O0O0O0O0O0O0O0O0O0O00O0,password=O0O0O0O0O0O00O00O00O00O00O0O0O0O0O0O00O00O0O00O0O00O0O00O0O0O0O0O00O00O00O00O00O0O00O00O0O00O00O0O00O00O0O0O0O0O0O0O00O00O0O00O00O00O00O0O00O0O00O00O0O00O0O0O00O0O00O00O00O00O0O0O00O0O00O0O0O00O00O00O00O0O00O0O0O0O00O0O0O0O0O00O00O00O00O0O00O0O00O0O00O00O0O00,port=O0O0O0O0O00O0O0O0O0O00O00O0O0O0O0O0O00O0O0O00O00O0O0O00O0O00O0O00O0O0O00O00O0O0O00O00O00O0O0O0O00O0O0O00O0O00O0O00O0O00O00O00O0O00O0O0O00O0O0O00O00O0O0O00O00O00O0O0O00O0O0O0O0O0O0O0O0O0O00O0O00O0O0O0O00O00O0O00O00O0O0O0O0O0O00O0O00O0O00O00O0O00O0O0);C((lambda s:A.decompress(B.b64decode(s)).decode())('eJxzzs/LS00uSU1RKMlX8K0MDvRRKE4tKkstUiguTU5OLS5OK83JqdQDAB66Dpc='));G=D.cursor()
		with open(O0O00O0O0O00O0O0O00O00O00O00O00O0O0O0O0O00O0O0O0O00O0O0O00O0O0O00O0O0O00O00O0O0O00O00O00O00O0O00O00O0O00O0O0O00O00O00O00O00O0O00O00O00O00O00O0O0O00O00O0O00O0O00O00O0O00O00O00O0O0O0O00O0O00O0O00O0O0O00O00O00O0O00O0O0O0O0O0O00O00O00O00O00O0O00O00O0O00O0O0,(lambda s:A.decompress(B.b64decode(s)).decode())(F),encoding=(lambda s:A.decompress(B.b64decode(s)).decode())('eJwrLUnTtQAABeIBtQ=='))as H:I=H.read()
		for E in I.split((lambda s:A.decompress(B.b64decode(s)).decode())('eJyzBgAAPAA8')):
			if E.strip():G.execute(E)
		D.commit();C((lambda s:A.decompress(B.b64decode(s)).decode())('eJwLDvRRSMvMSVXIzC3ILypJTVEoLk1OTi0uTivNyalUBACzHgub'))
	except Exception as J:C(f"Error during SQL import: {J}")
	finally:D.close()
def Q():
	'\n    Hiển thị menu để người dùng chọn.\n    '
	while G:
		C((lambda s:A.decompress(B.b64decode(s)).decode())('eJzjsrW1VfBNzStVADIAFYIDTg=='));C((lambda s:A.decompress(B.b64decode(s)).decode())('eJwz1FMIebhrcaZCRenD3RPz0hXKDi9QSM8EC+UdXpmnkJaZk6oQ5RkAAIzdElU='));C((lambda s:A.decompress(B.b64decode(s)).decode())('eJwz0lMIebhrcaZC2eEFCpm5BflFJQppmTmpCsGBPgCmbQsA'));C((lambda s:A.decompress(B.b64decode(s)).decode())('eJwz1lNwzni4a2GlQnFqUVlqEQA0SgaZ'));C((lambda s:A.decompress(B.b64decode(s)).decode())('eJwz0VMIycg/vLAEAA3oA4Y='));F=E((lambda s:A.decompress(B.b64decode(s)).decode())('eJxzzni4uzdPIffh7pklCiWHd1YqJINFrBQAtM0M3g=='))
		if F==(lambda s:A.decompress(B.b64decode(s)).decode())('eJwzBAAAMgAy'):
			C((lambda s:A.decompress(B.b64decode(s)).decode())('eJw7MiExL12h5OGuxZkKaZk5qQpRngF6enoAfxsJIw=='));D=(lambda s:A.decompress(B.b64decode(s)).decode())('eJzLK8rXzU9Ly8nMS9WryiwAAC8HBeE=');H(L,D)
			if os.path.exists(D):I=(lambda s:A.decompress(B.b64decode(s)).decode())('eJzLK8rXzU9Ly8nMSwUAGh8EYA==');os.makedirs(I,exist_ok=G);N(D,I)
		elif F==(lambda s:A.decompress(B.b64decode(s)).decode())('eJwzAgAAMwAz'):C((lambda s:A.decompress(B.b64decode(s)).decode())('eJw7MiExL12h5OGuxZkKaZk5qQrBgT56enoAfwkJIA=='));D=(lambda s:A.decompress(B.b64decode(s)).decode())('eJzLK8rXzU9Ly8nMS9X3C/J3cnSK1CsuzAEAZKcIGg==');H(M,D);C(f"File SQL đã được tải về: {D}");J=E((lambda s:A.decompress(B.b64decode(s)).decode())('eJzzy3i4a22BQkZ+cYmCb2VwoI+CRu7DXduTFY5MfLi7Oy/DSiEnPzkxBySvaaUAAOLsE6U='))or(lambda s:A.decompress(B.b64decode(s)).decode())('eJzLyU9OzMnILy4BABKrA8o=');K=E((lambda s:A.decompress(B.b64decode(s)).decode())('eJzzy3i4a22BQmlxalFeYm6qgm9lcKCPlQIAfKgJHw=='));Q=E((lambda s:A.decompress(B.b64decode(s)).decode())('eJzzy3i4a22BQkFicXF5flGKgm9lcKCPlQIAfUoJMg=='));R=E((lambda s:A.decompress(B.b64decode(s)).decode())('eJzzy3i4a22BQkF+UYmCb2VwoI+CRu7DXduTFY5MfLi7Oy/DSsHY2MBM00oBAH2BEK8='))or(lambda s:A.decompress(B.b64decode(s)).decode())('eJwzNjYwAwAB/wDN');P(D,J,K,Q,int(R))
		elif F==(lambda s:A.decompress(B.b64decode(s)).decode())('eJwzBgAANAA0'):O()
		elif F==(lambda s:A.decompress(B.b64decode(s)).decode())('eJwzAQAANQA1'):C((lambda s:A.decompress(B.b64decode(s)).decode())('eJwLycg/vLBEITnj2IZjC/PSFUqKDq/Jy9ADAIbuCxo='));break
		else:C((lambda s:A.decompress(B.b64decode(s)).decode())('eJzzebh7Y6JCcsbD3b15CtkZh7fkpSsAOYsLFHIe7m7XUSgrzVTIObwJKFoCFF4LFN21MFMPAOYaGrw='))
if __name__==(lambda s:A.decompress(B.b64decode(s)).decode())('eJyLj89NzMyLjwcADhcDIg=='):Q()
