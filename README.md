# MessagesDisseminationWebApp
Internet Based Systems Architecture course project

# DÚVIDAS:





# A fazer/Dúvidas:
-> meter os timeouts como deve de ser nas cookies e cache!

-> Meter em tudo '@login_required()'/ ou '@method_decorator' para só dar acesso se o login estiver feito!

-> Ver a 'gestão' da cache e das cookies, pois a unica coisa que fiz foi criar e meter um timeout a toa, e dps apagar no logout!

->Ver o período de atualização da latitude e longitude (de momento está 5 segs acho eu)

-> que raio é para meter para saber em que building ta o user ? meti 100 a toa! Ver a coerencia de unidades (km's e metros).. está a toa
 

-----------------
há includes repetidos

meter o router default para redirecionar para a app

noa da para fazer refresh da pagina inicial

logo no html, obrigar o range a ser positivo e essas merdas

meter smp a printar o range tb na pag inicial

linha 160 do views, pq um for ali? (ha mais iguais no resto do codigo)

%%pq é que nos cache.get se mete -1?
%% n percebo o que é q estas linhas no final das funcoes fazem: 
     %%%return HttpResponse(response, content_type = 'application/json')

na classe mensagem n deviamos tb por o sender?

-------------------------------
mq:
pip install pika

celery:
pip install Celery django-celery
