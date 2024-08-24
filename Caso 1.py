import numpy as np

np.random.seed(2024)

CP = 1150
RC = 8905
RP = 72.3
RO = 15.2
RTC = 4.7

media = 80.5
sd = 87.2

def isp(cb, rc):
    return cb / (rc + 10 * (RP + RO + RTC))

alfa = (media / sd) ** 2
beta = (sd ** 2) / media
perdidas = np.random.gamma(alfa, beta, 100000)

rendimientos = 8050 * 0.03 + 976 * 0.01

cb_f = CP + rendimientos - perdidas
rc_f = RC - perdidas

isps = isp(cb_f, rc_f)

media_isp = np.mean(isps)
mediana_isp = np.median(isps)
sd_isp = np.std(isps)
min_isp = np.min(isps)
max_isp = np.max(isps)
percentil_1 = np.percentile(isps, 1)
percentil_99 = np.percentile(isps, 99)

print("Resumen")
print(f"Media: {media_isp:.4f}")
print(f"Mediana: {mediana_isp:.4f}")
print(f"Desviación estándar: {sd_isp:.4f}")
print(f"Mínimo: {min_isp:.4f}")
print(f"Máximo: {max_isp:.4f}")
print(f"Primer percentil: {percentil_1:.4f}")
print(f"Percentil 99: {percentil_99:.4f}")

prob_irregularidad = np.mean(isps < 0.10)
print(f"Probabilidad de entrar en irregularidad: {prob_irregularidad:.4f}")