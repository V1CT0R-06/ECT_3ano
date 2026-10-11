# RC1 — Mini-Teste (Guiões 1 e 2): vídeos confirmados + plano completo

> Objetivo: estudar **toda a matéria relevante até ao fim do Guião Prático 2** de Redes de Comunicação I, usando vídeos em inglês e evitando conteúdo posterior como VLANs avançadas, STP, RIP, OSPF, NAT, DHCP e IPv6.

## Âmbito confirmado do mini-teste

Com base nos Guiões Práticos 1 e 2 e nos slides teóricos do projeto, deves dominar:

- configuração IPv4 básica de hosts e interfaces de router;
- endereços IPv4, máscaras e subnetting;
- network address, broadcast, first host, last host e número de hosts;
- saber decidir se dois hosts estão ou não na mesma rede;
- interfaces físicas e endereços Ethernet/MAC;
- Ethernet e switching básico;
- MAC address table;
- learning, flooding e forwarding;
- encapsulamento:
  - ICMP dentro de IPv4;
  - IPv4 dentro de Ethernet;
- ARP:
  - ARP Request;
  - ARP Reply;
  - ARP cache/table;
  - broadcast ARP;
  - resolução IP -> MAC;
- comunicação dentro da mesma subnet;
- comunicação entre subnets;
- default gateway;
- diferença entre endereço IP e endereço MAC ao longo de um percurso;
- routing básico;
- routing table;
- directly connected routes;
- forwarding por routers;
- ICMP;
- ping:
  - Echo Request;
  - Echo Reply;
  - sequence number;
  - RTT;
- traceroute;
- TTL;
- IPv4 header, sobretudo os campos relevantes para a matéria;
- MTU;
- fragmentação e reassembly IPv4:
  - Total Length;
  - Identification;
  - DF;
  - MF;
  - Fragment Offset;
  - cálculo do tamanho dos fragmentos;
- Ethernet MTU típica de 1500 bytes;
- padding Ethernet / payload mínimo;
- interpretação básica de capturas no Wireshark;
- comandos básicos usados nos guiões:
  - `ping`;
  - `arp`;
  - `traceroute` / `tracert`;
  - `show ip route`;
  - `show ip interface brief`.

---

# Conjunto de vídeos recomendado

## 1. Subnetting — série principal

### Practical Networking — What is Subnetting? - Subnetting Mastery - Part 1 of 7

https://www.youtube.com/watch?v=BWZ-MHIhqjM

**Confirmado:** o vídeo existe no YouTube e é do canal Practical Networking.

### O que cobre

- conceito de subnetting;
- CIDR;
- subnet mask;
- Network ID;
- Broadcast IP;
- First Host;
- Last Host;
- Next Network;
- número de endereços de uma subnet.

### Para o mini-teste

Este vídeo é essencial, mas **não chega sozinho**. Continua pela série.

A série é:

1. What is Subnetting? - Part 1
2. Drawing the Cheat Sheet - Part 2
3. How to solve ANY Subnetting Problems in 60 seconds or less - Part 3
4. Practice Examples - Part 4
5. Time-Saving Tricks - Part 5
6. Subnetting in the /17 - /24 range - Part 6
7. Subnetting in the /1 - /16 range - Part 7

Playlist / pesquisa pelo nome da série:
https://www.youtube.com/results?search_query=Practical+Networking+Subnetting+Mastery

### O que tens de conseguir fazer depois

Dado, por exemplo:

`192.168.1.70/27`

deves conseguir determinar:

- máscara;
- Network Address;
- Broadcast Address;
- First Host;
- Last Host;
- quantidade de hosts;
- se outro endereço pertence à mesma subnet.

**Prioridade:** MUITO ALTA.

---

# 2. Hosts na mesma rede e em redes diferentes

## Practical Networking — Everything Hosts do to speak on the Internet - Part 1

https://www.youtube.com/watch?v=gYN2qN11-wE

**Confirmado diretamente no YouTube.**

### Conteúdo

Mostra o que um host faz para comunicar com outro host, incluindo:

- análise da rede de destino;
- uso da subnet mask;
- comunicação local;
- ARP;
- resolução IP -> MAC;
- construção da frame Ethernet;
- diferença entre Layer 2 e Layer 3;
- comportamento quando os hosts estão ligados direta ou indiretamente.

**Prioridade:** MUITO ALTA.

---

## Practical Networking — Everything Hosts do to speak on the Internet - Part 2

https://www.youtube.com/watch?v=JI9Zm2tbUoE

**Confirmado diretamente no YouTube.**

### Conteúdo

Continua o vídeo anterior e é especialmente importante para:

- comunicação com uma **foreign network**;
- decidir que o destino não está na subnet local;
- uso do **default gateway**;
- ARP para obter o MAC do next-hop/default gateway;
- IP de destino continuar a ser o host final;
- MAC de destino corresponder ao próximo salto Ethernet.

### Ideia fundamental para o mini-teste

Quando o destino está noutra rede:

- **Destination IP** = host final;
- **Destination MAC** = interface do router/default gateway naquele segmento.

Os IPs representam os extremos da comunicação.

Os MACs são usados **salto a salto**.

**Prioridade:** MUITO ALTA.

---

# 3. ARP

## PowerCert Animated Videos — ARP Explained - Address Resolution Protocol

https://www.youtube.com/watch?v=cn8Zxh9bPio

**Vídeo confirmado.**

### Conteúdo

- significado de ARP;
- IP address vs MAC address;
- ARP cache;
- ARP Request;
- ARP Reply;
- broadcast ARP;
- descoberta do MAC correspondente a um IPv4;
- entradas dinâmicas da ARP table.

### Tens de saber

Exemplo, mesma subnet:

`PC1 quer enviar para PC2`

Se não conhece o MAC de PC2:

1. verifica ARP cache;
2. envia ARP Request em broadcast;
3. PC2 responde com ARP Reply;
4. PC1 guarda IP -> MAC;
5. envia a Ethernet frame.

Noutra subnet:

1. PC1 percebe que o destino é remoto;
2. procura o MAC do **default gateway**, não o MAC do host remoto;
3. envia a frame ao router.

**Prioridade:** MUITO ALTA.

---

# 4. Switching / Ethernet

## Practical Networking — Everything Switches do - Part 1

https://www.youtube.com/watch?v=AhOU2eOpmX0

**Confirmado diretamente no YouTube.**

### Conteúdo

- switch como dispositivo Layer 2;
- MAC Address Table;
- **Learning**;
- **Flooding**;
- **Forwarding**;
- diferença entre enviar tráfego **through a switch** e **to a switch**.

### Porque está no mini-teste

O Guião 2 indica explicitamente:

- Ethernet technology;
- Switching.

Logo, switching básico faz parte do âmbito.

### Tens de saber

Um switch aprende:

`Source MAC -> incoming port`

Depois, para o Destination MAC:

- se conhece a porta -> Forward;
- se não conhece -> Flood;
- broadcast -> Flood.

**Prioridade:** ALTA.

---

## Practical Networking — Everything Switches do - Part 2

https://www.youtube.com/watch?v=G7GyWjJtjNs

**Confirmado diretamente no YouTube.**

### O que interessa deste vídeo

- Unicast Flooding;
- Broadcasts;
- comunicação por vários switches.

### ATENÇÃO

O vídeo também introduz **VLANs**.

Para este mini-teste, **não precisas de estudar VLANs** se o âmbito termina no Guião 2.

Podes ver a parte de flooding/broadcasts e ignorar a parte aprofundada de VLANs.

**Prioridade:** MÉDIA.

---

# 5. Routing e forwarding

## Practical Networking — Everything Routers do - Part 1

https://www.youtube.com/watch?v=AzXys5kxpAM

O vídeo faz parte da série oficial Networking Fundamentals da Practical Networking.

### Conteúdo relevante

- conceito de routing;
- routing table;
- como um router sabe que redes estão ligadas;
- rotas;
- decisão de encaminhamento.

**Prioridade:** ALTA.

---

## Practical Networking — Everything Routers do - Part 2 - How Routers forward Packets

https://www.youtube.com/watch?v=Ep-x_6kggKA

**Confirmado diretamente no YouTube.**

### Conteúdo

- utilização da Routing Table;
- utilização da ARP Table pelo router;
- encaminhamento de um pacote;
- escolha da interface de saída;
- ARP no segmento seguinte;
- reconstrução da frame Ethernet;
- percurso de ida;
- percurso de resposta.

Este é extremamente próximo dos exercícios do Guião 2.

### Tens de perceber perfeitamente

Num router:

1. recebe uma Ethernet frame;
2. retira a frame Ethernet;
3. examina o Destination IP;
4. consulta a routing table;
5. escolhe a interface/next hop;
6. se necessário usa ARP;
7. cria **uma nova Ethernet frame**;
8. envia o mesmo pacote IP em direção ao destino.

O TTL IPv4 é reduzido ao atravessar routers.

**Prioridade:** MUITO ALTA.

---

# 6. Vídeo que junta hosts + switches + routers + ARP + routing

## Practical Networking — How Data moves through the Internet - Networking Fundamentals

https://www.youtube.com/watch?v=YJGGYKAV4pA

**Confirmado. Duração aproximada: 26:46.**

### Conteúdo

Este é o melhor vídeo de revisão do conjunto.

Mostra em conjunto:

- Routing Table;
- ARP Table;
- MAC Address Table;
- Host A -> Host B;
- resposta Host B -> Host A;
- Host A -> Host C;
- comunicação local;
- comunicação através de routers;
- ARP;
- switching;
- routing;
- packet forwarding;
- alterações das frames Ethernet ao longo do percurso.

### Capítulos confirmados

- 01:03 — Routing Table, ARP Table, MAC Address Table
- 02:55 — Populating Routing Tables
- 04:51 — Packet details Host A -> Host B
- 05:48 — Packet #1 Host A -> Host B
- 14:23 — Response Host B -> Host A
- 17:28 — Packet #2 Host A -> Host C
- 21:34 — Response Host C -> Host A

### Como usar

Não recomendo vê-lo como primeiro vídeo.

Vê primeiro:

- subnetting;
- hosts;
- ARP;
- switching;
- routers.

Depois usa este como **revisão final**.

**Prioridade:** MUITO ALTA.

---

# 7. ICMP e PING

## PowerCert Animated Videos — PING Command - Troubleshooting Networks

https://www.youtube.com/watch?v=IIicPE38O-s

**Confirmado diretamente no YouTube.**

### Conteúdo

- comando `ping`;
- conectividade;
- ICMP;
- Echo Request;
- Echo Reply;
- interpretação de respostas;
- troubleshooting básico.

### Para a cadeira tens ainda de saber

O `ping` usa:

- ICMP Echo Request — Type 8;
- ICMP Echo Reply — Type 0.

No Guião 2 também observas:

- periodicidade dos ICMP packets;
- Sequence Number;
- RTT.

O ICMP está encapsulado num datagrama IPv4.

**Prioridade:** ALTA.

---

# 8. Traceroute e TTL

## PowerCert Animated Videos — Traceroute (tracert) Explained - Network Troubleshooting

https://www.youtube.com/watch?v=up3bcBLZS74

**Confirmado diretamente no YouTube.**

### Conteúdo

- `traceroute` / `tracert`;
- rota seguida pelos packets;
- routers no percurso;
- hops;
- utilização para troubleshooting.

### Para o mini-teste associa isto ao TTL

O campo IPv4 **TTL** é reduzido pelos routers.

Quando chega a 0, o router elimina o datagrama.

Isto permite ao traceroute descobrir sucessivamente os routers do caminho.

**Prioridade:** ALTA.

---

# 9. Fragmentação IPv4 e MTU

## Fragmentation in IP packets & MTU Explained — Qnarik Korkotyan

https://www.youtube.com/watch?v=mFL51G02E5c

**Confirmado diretamente no YouTube. Publicado em 2026.**

### Conteúdo confirmado

- MTU;
- fragmentation;
- Ethernet MTU;
- IPv4 fragmentation;
- Total Length;
- Identification;
- Flags;
- DF;
- MF;
- Fragment Offset;
- reassembly;
- razões pelas quais ocorre fragmentação.

### Capítulos

- 00:35 — MTU
- 01:09 — Fragmentation
- 01:37 — quando e porquê ocorre
- 02:10 — campos do IPv4 Header usados na fragmentação
- 02:37 — reassembly

### Para o teu mini-teste isto é obrigatório

O Guião 2 usa explicitamente:

- Ethernet MTU típica = **1500 bytes**;
- ping com 2000 bytes;
- ping com 3100 bytes;
- explicar porque aparecem 2 ou 3 fragmentos;
- explicar os campos do cabeçalho;
- calcular o tamanho de cada fragmento.

### Regra importante

Assumindo um IPv4 header normal de 20 bytes:

`1500 - 20 = 1480 bytes`

Logo, cada fragmento completo pode transportar normalmente:

`1480 bytes de IPv4 payload`

E:

`Fragment Offset = posição inicial dos dados / 8`

Exemplo:

Fragmento 1:
- offset = 0;
- MF = 1.

Fragmento 2:
- começa no byte 1480;
- offset = `1480 / 8 = 185`;
- MF = 1 se ainda existir outro fragmento.

Último fragmento:
- MF = 0.

Todos os fragmentos do mesmo datagrama têm o mesmo:

`Identification`

**Prioridade:** MUITO ALTA.

---

# 10. IPv4 Header — o que estudar mesmo que os vídeos não o cubram todo

Os vídeos anteriores explicam vários campos do IPv4 header, mas para o mini-teste deves reconhecer estes diretamente dos slides da cadeira:

- Version;
- IHL;
- Total Length;
- Identification;
- Flags;
  - DF;
  - MF;
- Fragment Offset;
- TTL;
- Protocol;
- Header Checksum;
- Source IP Address;
- Destination IP Address.

## Campos mais importantes

### Total Length

Tamanho total do datagrama IPv4:

`header + payload`

### Identification

Identifica os fragmentos pertencentes ao mesmo datagrama original.

### DF — Don't Fragment

Se estiver a 1 e for necessária fragmentação, o datagrama não pode simplesmente ser fragmentado.

### MF — More Fragments

- `MF = 1` -> ainda existem fragmentos depois deste;
- `MF = 0` -> último fragmento.

### Fragment Offset

Posição dos dados do fragmento no datagrama original.

Unidade:

`8 bytes`

### TTL

É diminuído pelos routers.

### Protocol

Indica o protocolo transportado pelo IPv4.

Exemplos importantes:

- ICMP = 1;
- TCP = 6;
- UDP = 17.

---

# 11. Ethernet Frame — conteúdo que tens de saber

Para o Guião 2, reconhece pelo menos:

- Destination MAC;
- Source MAC;
- EtherType;
- Data/Payload;
- FCS.

## Encapsulamento

Para o ping:

```text
Ethernet Frame
└── IPv4 Datagram
    └── ICMP Message
```

Ou seja:

`ICMP -> IPv4 -> Ethernet`

---

# 12. Ethernet padding

Este é um detalhe do Guião 2 que é fácil esquecer.

O Ethernet payload tem um tamanho mínimo.

Para uma Ethernet frame normal, o payload mínimo é:

`46 bytes`

Quando os dados transportados são menores, é adicionado:

`Padding`

Isto pode aparecer numa captura do Wireshark.

---

# 13. Default Gateway

Se quiseres uma explicação visual adicional, procura:

**PowerCert Animated Videos — Default Gateway Explained**

Link conhecido:
https://www.youtube.com/watch?v=pCcJFdYNamc

### Regra fundamental

Se:

`Destination Network == Local Network`

o host envia diretamente ao destino.

Se:

`Destination Network != Local Network`

o host envia ao:

`Default Gateway`

O default gateway tem de ser uma interface de router que pertença à mesma rede física/IP do host.

---

# 14. Wireshark — o que tens de conseguir interpretar

Mesmo que os vídeos sejam o núcleo do estudo, deves abrir o Guião 2 no final e praticar as capturas.

Consegue identificar:

## Ethernet

- Source MAC;
- Destination MAC;
- EtherType.

## IPv4

- Source IP;
- Destination IP;
- TTL;
- Total Length;
- Identification;
- Flags;
- Fragment Offset;
- Protocol.

## ICMP

- Echo Request;
- Echo Reply;
- Sequence Number.

## ARP

- Request;
- Reply;
- Sender IP;
- Sender MAC;
- Target IP;
- Target MAC.

---

# 15. A pergunta clássica que tens de saber resolver

Considera:

```text
PC1 ---- Switch ---- Router ---- Switch ---- PC3
```

PC1:

```text
192.168.1.100/24
Gateway: 192.168.1.1
```

PC3:

```text
192.168.3.33/24
Gateway: 192.168.3.1
```

Se PC1 fizer:

```text
ping 192.168.3.33
```

tens de conseguir explicar:

1. PC1 aplica a sua máscara.
2. Descobre que `192.168.3.33` não pertence à rede `192.168.1.0/24`.
3. Decide enviar o pacote ao default gateway.
4. Se necessário, PC1 faz ARP para `192.168.1.1`.
5. O IP de destino continua a ser `192.168.3.33`.
6. A Destination MAC da primeira frame é a MAC da interface do Router na rede de PC1.
7. O switch encaminha a frame.
8. Router recebe a frame.
9. Router consulta a routing table.
10. Router descobre a rede `192.168.3.0/24`.
11. Se necessário, Router faz ARP por `192.168.3.33`.
12. Router cria uma nova Ethernet frame.
13. Source MAC passa a ser a MAC da interface de saída do Router.
14. Destination MAC passa a ser a MAC de PC3.
15. Source IP continua `192.168.1.100`.
16. Destination IP continua `192.168.3.33`.
17. PC3 recebe ICMP Echo Request.
18. PC3 responde com ICMP Echo Reply.
19. No retorno, Source IP = `192.168.3.33`.
20. Destination IP = `192.168.1.100`.

Se conseguires explicar isto sem consultar apontamentos, já tens uma grande parte do Guião 2 dominada.

---

# Ordem exata em que recomendo ver os vídeos

## Bloco A — IPv4 e subnetting

1. Subnetting Mastery Part 1
2. Part 2
3. Part 3
4. Part 4
5. Part 5
6. Part 6 e 7 se precisares de trabalhar máscaras fora do intervalo mais fácil

---

## Bloco B — Comunicação Ethernet/IP

7. Everything Hosts do — Part 1  
   https://www.youtube.com/watch?v=gYN2qN11-wE

8. Everything Hosts do — Part 2  
   https://www.youtube.com/watch?v=JI9Zm2tbUoE

9. ARP Explained  
   https://www.youtube.com/watch?v=cn8Zxh9bPio

---

## Bloco C — Switching e Routing

10. Everything Switches do — Part 1  
    https://www.youtube.com/watch?v=AhOU2eOpmX0

11. Everything Switches do — Part 2  
    https://www.youtube.com/watch?v=G7GyWjJtjNs  
    **Ignorar/adiar VLANs.**

12. Everything Routers do — Part 1  
    https://www.youtube.com/watch?v=AzXys5kxpAM

13. Everything Routers do — Part 2  
    https://www.youtube.com/watch?v=Ep-x_6kggKA

---

## Bloco D — ICMP

14. PING Command  
    https://www.youtube.com/watch?v=IIicPE38O-s

15. Traceroute  
    https://www.youtube.com/watch?v=up3bcBLZS74

---

## Bloco E — Fragmentação

16. Fragmentation in IP packets & MTU Explained  
    https://www.youtube.com/watch?v=mFL51G02E5c

---

## Bloco F — Revisão final

17. How Data moves through the Internet  
    https://www.youtube.com/watch?v=YJGGYKAV4pA

---

# Matriz de cobertura da matéria

| Matéria | Vídeo principal |
|---|---|
| IPv4 addressing | Subnetting Mastery + Hosts |
| Subnet masks | Subnetting Mastery |
| CIDR | Subnetting Mastery |
| Network address | Subnetting Mastery |
| Broadcast | Subnetting Mastery |
| First/Last Host | Subnetting Mastery |
| Mesma subnet / subnet diferente | Hosts Part 1/2 |
| Default Gateway | Hosts Part 2 |
| MAC vs IP | Hosts + ARP + Data moves |
| ARP Request/Reply | ARP Explained |
| ARP cache | ARP Explained |
| Ethernet | Hosts + Switches |
| Switching | Switches Part 1 |
| Learning | Switches Part 1 |
| Flooding | Switches Part 1/2 |
| Forwarding | Switches Part 1 |
| MAC Address Table | Switches + Data moves |
| Routing Table | Routers + Data moves |
| IP Routing | Routers Part 1/2 |
| Forwarding | Routers Part 2 |
| ICMP | PING |
| Echo Request/Reply | PING |
| RTT | PING + Guião 2 |
| Traceroute | Traceroute |
| TTL | Traceroute + IPv4 slides |
| Encapsulation | Hosts + Data moves + Guião 2 |
| IPv4 fragmentation | Fragmentation video |
| MTU | Fragmentation video |
| Identification | Fragmentation video |
| DF/MF | Fragmentation video |
| Fragment Offset | Fragmentation video |
| Reassembly | Fragmentation video |
| Wireshark | praticar diretamente no Guião 2 |
| Ethernet padding | Guião 2 / slides |
| Cisco/VPC commands | Guiões 1 e 2 |

---

# O que NÃO estudar agora

Se o mini-teste termina no conteúdo dado até ao Guião 2, não gastes tempo agora com:

- VLAN configuration;
- 802.1Q;
- trunks;
- STP / RSTP;
- RIP;
- OSPF;
- BGP;
- VRRP;
- NAT;
- DHCP em detalhe;
- IPv6;
- Wi-Fi;
- sockets;
- aplicações;
- TCP em detalhe;
- UDP em detalhe.

Alguns vídeos podem mencionar estes assuntos. Não significa que tenhas de os estudar já.

---

# Checklist final antes do mini-teste

Marca cada um quando conseguires explicar sem ajuda.

## IPv4 / Subnetting

- [ ] Sei converter `/24`, `/25`, `/26`, `/27`, `/28`, `/29`, `/30` para máscaras.
- [ ] Sei calcular Network Address.
- [ ] Sei calcular Broadcast.
- [ ] Sei calcular First Host.
- [ ] Sei calcular Last Host.
- [ ] Sei calcular número de hosts.
- [ ] Sei decidir se dois IPs pertencem à mesma subnet.

## Ethernet / ARP

- [ ] Sei distinguir IP de MAC.
- [ ] Sei explicar ARP Request.
- [ ] Sei explicar ARP Reply.
- [ ] Sei explicar ARP cache.
- [ ] Sei explicar porque o ARP Request é broadcast.
- [ ] Sei dizer qual MAC aparece como destino numa ligação local.
- [ ] Sei dizer qual MAC aparece quando o destino é remoto.

## Switching

- [ ] Sei explicar MAC Address Table.
- [ ] Sei explicar Learning.
- [ ] Sei explicar Flooding.
- [ ] Sei explicar Forwarding.
- [ ] Sei explicar o que acontece a um broadcast.

## Routing

- [ ] Sei explicar default gateway.
- [ ] Sei interpretar uma routing table básica.
- [ ] Sei explicar directly connected routes.
- [ ] Sei explicar como o router escolhe a interface de saída.
- [ ] Sei explicar que os MACs mudam entre segmentos.
- [ ] Sei explicar que os IPs dos hosts finais normalmente permanecem os mesmos durante o encaminhamento.

## ICMP

- [ ] Sei o que é ICMP.
- [ ] Sei o que é Echo Request.
- [ ] Sei o que é Echo Reply.
- [ ] Sei para que serve ping.
- [ ] Sei o significado de RTT.
- [ ] Sei o papel do Sequence Number.
- [ ] Sei explicar traceroute.
- [ ] Sei explicar TTL.

## Encapsulamento

- [ ] Sei que ICMP está dentro de IPv4.
- [ ] Sei que IPv4 está dentro de Ethernet.
- [ ] Sei identificar Source/Destination MAC.
- [ ] Sei identificar Source/Destination IP.

## Fragmentação

- [ ] Sei o que é MTU.
- [ ] Sei que Ethernet normalmente usa MTU 1500.
- [ ] Sei calcular `1500 - 20 = 1480`.
- [ ] Sei explicar Identification.
- [ ] Sei explicar DF.
- [ ] Sei explicar MF.
- [ ] Sei calcular Fragment Offset em unidades de 8 bytes.
- [ ] Sei identificar o último fragmento.
- [ ] Sei explicar reassembly.
- [ ] Sei calcular quantos fragmentos são necessários.

## Wireshark / prática

- [ ] Sei reconhecer Ethernet, IPv4, ARP e ICMP no Wireshark.
- [ ] Sei usar filtros básicos.
- [ ] Sei interpretar um ping numa captura.
- [ ] Sei interpretar um ARP Request/Reply.
- [ ] Sei interpretar fragmentos IPv4.
- [ ] Sei justificar um ping que funciona ou falha por falta de gateway.

---

# Estratégia de estudo recomendada

## Primeira passagem

Vê os vídeos sem tentar decorar.

Objetivo:

**perceber o percurso de um pacote.**

---

## Segunda passagem

Faz o Guião 2 e tenta responder antes de olhar para resultados anteriores.

Em cada packet pergunta:

1. Qual é o Source IP?
2. Qual é o Destination IP?
3. Qual é o Source MAC?
4. Qual é o Destination MAC?
5. Estão na mesma subnet?
6. É necessário default gateway?
7. É necessário ARP?
8. Que tabela é consultada?
9. O switch faz flooding ou forwarding?
10. O router recebe este packet?
11. O TTL muda?
12. Existe fragmentação?

---

## Terceira passagem

Faz subnetting sem calculadora e exercícios de fragmentação.

---

## Última revisão

Vê:

**How Data moves through the Internet**

https://www.youtube.com/watch?v=YJGGYKAV4pA

Depois tenta explicar sozinho um percurso:

`PC -> Switch -> Router -> Switch -> PC`

incluindo ida **e retorno**.

---

# Nota importante sobre cobertura

Os vídeos cobrem muito bem os conceitos de rede.

No entanto, existem alguns detalhes **específicos da cadeira e dos Guiões 1/2** que deves rever diretamente nos materiais da UA:

- comandos exatos de Cisco/VPC;
- utilização específica do GNS3;
- opções/filtros específicos do Wireshark;
- Ethernet padding observado nas capturas;
- valores e campos específicos pedidos nas perguntas do Guião;
- exercícios concretos de fragmentação com 2000 e 3100 bytes.

Por isso, a combinação mais segura é:

**vídeos acima + fazer novamente o Guião 2 + rever os slides `1_1 - Redes IP` e `Redes IP_Sub-Redes`.**

Assim não dependes de nenhum vídeo externo para um detalhe específico que o professor possa ter dado em aula.
