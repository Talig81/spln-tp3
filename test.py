from initial import Poema, contaMetrica

poema_body = """
A princípio é simples, anda-se sozinho
Passa-se nas ruas bem devagarinho
Está-se bem no silêncio e no burburinho
Bebe-se as certezas num copo de vinho
E vem-nos à memória uma frase batida
Hoje é o primeiro dia do resto da tua vida

Pouco a pouco o passo faz-se vagabundo
Dá-se a volta ao medo, dá-se a volta ao mundo
Diz-se do passado, que está moribundo
Bebe-se o alento num copo sem fundo
E vem-nos à memória uma frase batida
Hoje é o primeiro dia do resto da tua vida

E é então que amigos nos oferecem leito
Entra-se cansado e sai-se refeito
Luta-se por tudo o que se leva a peito
Bebe-se, come-se e alguém nos diz: Bom proveito
E vem-nos à memória uma frase batida
Hoje é o primeiro dia do resto da tua vida

Depois vêm cansaços e o corpo fraqueja
Olha-se para dentro e já pouco sobeja
Pede-se o descanso, por curto que seja
Apagam-se dúvidas num mar de cerveja
E vem-nos à memória uma frase batida
Hoje é o primeiro dia do resto da tua vida

Enfim duma escolha faz-se um desafio
Enfrenta-se a vida de fio a pavio
Navega-se sem mar, sem vela ou navio
Bebe-se a coragem até dum copo vazio
E vem-nos à memória uma frase batida
Hoje é o primeiro dia do resto da tua vida

E entretanto o tempo fez cinza da brasa
E outra maré cheia virá da maré vaza
Nasce um novo dia e no braço outra asa
Brinda-se aos amores com o vinho da casa
E vem-nos à memória uma frase batida
Hoje é o primeiro dia do resto da tua vida
"""

poema = Poema(poema_body)
assert poema.n_estrofes == 6
assert poema.estrofes[0].n_versos == 6
assert contaMetrica(poema.estrofes[0].versos[1].body) == 12


print("yay")