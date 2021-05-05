from hashlib import sha256
import time as t

#CODIFICAR

def aplicar_sha256(text):
	return sha256(text.encode("ascii")).hexdigest()

#AQUI ELE CONCATENA OS DADOS INSERIDOS
#TESTAR OS NONCES POSSIVEÍS

def minerar(num_bloco, transacoes, hash_ant, quant_zeros):
	nonce = 0
	while True:
		text = str(num_bloco) + transacoes + hash_ant + str(nonce)
		meu_hash = aplicar_sha256(text)

		if meu_hash.startswith("0" * quant_zeros):
			return nonce, meu_hash
		nonce += 1

if __name__ == "__main__":
	num_bloco = 682074		#VARIAVÉL
	transacoes = """
bc1q4pq4zg7psdjfk4rqvv3cq3ef9vqd48rzpl9ttg
5.26274317 BTC
35Lov749zSdxEdqMypG2tHX2TSCVsF1kUH
0.00874600 BTC
3LKwvPz4wPo7sEqKjMV8P6gKtM6pnbsTu3
0.01865230 BTC
bc1qg3ss8dhkza2558s83erc2ajwm6k99ycaja4w3x
0.06000000 BTC
bc1qnuve0mwje4tk2h9uq45vq2ftnsthgc8ey5yc00
0.13123266 BTC
bc1q0ngtrrhcnzpwty6ye367rxlmv2hhe530hw4n8m
5.04251221 BTC
1PyUuCsPHYGKTRSAaNS4W8ABWM5T8YeXvy
0.02225686 BTC
3NfVAqP8U1Dpa9raECJYor72bFX71Fgh9i
0.00750000 BTC
1DAKS7RBWiyDXSwnzzUkYWbKxMLYQFNh5e
0.01372486 BTC"""

	quant_zeros = 2 #VARIAVÉL

	hash_ant = "0000000000000000000303fad3595cd3c1120ac1f9b2ef80534bc5719ceba54d" #VARIAVÉL

	t_i = t.time() #TEMPO EM SEGUNDOS

	result = minerar(num_bloco, transacoes, hash_ant, quant_zeros)

	print(result)

	print("%1.2fsegs" %(t.time() - t_i))
