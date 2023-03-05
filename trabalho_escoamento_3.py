# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 13:04:26 2023

@author: Usuário
"""

importar  numpy  como  np
importar  matemática  como  mt

# VARIÁVEIS DE ENTRADA:
do  =  # valores a serem fornecidos pelo exemplo
dg  =  # valores a serem fornecidos pelo exemplo
S  =  # salinidade a ser acomodada pelo exemplo
Mg  =  # Massa a ser acomodada pelo exemplo
Pb  =  # Pressão de Bolha a ser acomodado pelo exemplo ????
# Tpc e Ppc serão dados na entrada da tabela - Temperatura crítica será sempre a mesma?

# Pressões e Temperatura e Referência

# dúvida: sofrerão diversas pressões na tabela e apenas uma temperatura, bem como apenas uma única temperatura crítica. As críticas pressóricas serão diversas para cada uma variar com cada pressão térmica, ou será apenas uma que vai calcular parar todas as pressóricas?


# Pressão e Tempratura Pseudocríticas


# Pressão de Bolha
API  =  141.5  /  do  -  131.5    # será um único grau API

a_pb  = ( 7.916  *  10  *  - 4 ) * ( API  **  1.5410 ) - ( 4.561  *  10  -  5 ) * ( T  *  1.3911 )   # T em F

# Razão de Solubilidade gás-óleo

#np.zeros(lenght Pvec)


for  i  in  range ( 0 , len ( Pvec )):    # número de linhas deve ser o mesmo do número de pressão que será usado
    se  P  >  Pb :
    a_rsb [ i ] = ( 7.916  *  10  *  - 4 ) * ( API  **  1.541 ) - ( 4.561  *  10  -  5 ) * ( T  **  1.3911 )   # T em F, vai calcular o parâmetro a para a linha da vez
    rsb [ i , 3 ] = ((( Pb  /  112.727 ) +  12.34 ) * ( dg  **  0.8439 ) * ( 10  *  a_rsb [ i ])) **  1.73184   # P em psia e T em F, vai calular a razão de solubilidade (p/ P>Pb) e salve na linha da vez e na coluna 3
    pb [ i , 2 ] = (( 112.727  * ( rsb [ i , 3 ] *  0.577421 )) / (( dg  **  0.8439 ) *  10  *  a_pb )) -  1391.051   # T em F, vai calcular a pressão de bolha e salvar na linha da vez e na coluna 2 usando a razão de solubilidade que esta na linha da vez e na coluna 3
    elif  P  <=  Pb :
    a_rs [ i ] = ( 7.916  *  10  *  - 4 ) * ( API  **  1.541 ) - ( 4.561  *  10  -  5 ) * ( T  **  1.3911 )   # T em F, vai calcular o parâmetro a para a linha da vez
    rs [ i , 3 ] = ((( P [ i , 1 ] /  112.727 ) +  12.34 ) * ( dg  **  0.8439 ) * ( 10  *  a_rs [ i ])) **  1.73184   # P em psia e T em F , vai calcular a razão de solubilidade (p/ P<=Pb) e guardar na linha da vez e na coluna 3
    pb [ i , 2 ] = (( 112.727  * ( rs [ i , 3 ] *  0.577421 )) / (( dg  **  0.8439 ) *  10  *  a_pb )) -  1391.051   # T em F, vai calular a pressão de bolha e salvar na linha da vez e coluna 2

# Compressibilidade Isotérmica do Óleo
para  i  no  intervalo ( 0 , len ( Pvec )):
    se  P  >=  Pb :
        co [ i , 4 ] =  1.705  * ( 10  *  - 7 ) * ( rs [ i , 3 ] **  0.69357 ) * ( dg  **  0.1885 ) * ( API  **  0.3272 ) * ( T  **  0.6729 ) * ( P [ i , 1 ] **  - 0.5906 )  # T em F, vai calcular a compressibilidade isotérmica (p/ P>=Pb) e salvar na linha da vez e coluna 4 usando a razão de solubilidade que esta na linha da vez e na coluna 3 e pressão da linha da vez e que esta na coluna 1
    elif  P  <  Pb :
    #derivada

# Fator Volume-Formação
para  i  no  intervalo ( 0 , len ( Pvec )):
    se  P  >  Pb :
        bob [ i ] =  1.0113  + ( 7.2046  *  10  *  - 5 ) * (( rsb [ i , 3 ] **  0.3738 ) * ( dg  **  0.2914  /  do  **  0.6265 ) +  0.24626  * ( T  **  0.5371 )) **  3.0936 )  # T em F, usamos rsb, pois é a razão de solubilidade na pressão de bolha anterior. Vai calcular o fato volume formação no ponto de bolha da linha da vez usando a razão de solubilidade na pressão de bolha que esta na linha da vez e na coluna 3
        bo  =  bob  *  np . exp ( - co  * ( P [ i , 1 ] -  Pb ))    # vai calcular o fator volume formação (p/ P>Pb) e guardar na linha da vez e na coluna 5
    elif  P  <=  Pb :
        bo  =  1.0113  + ( 7.2046  *  10  **  - 5 ) * (( rs [ i , 3 ] **  0.3738 ) * ( dg  **  0.2914  /  do  **  0.6265 ) +  0.24626  * ( T  **  0.5371 )) **  3.0936 )  # T em F, vai calcular o fator volume formação (p/ P<=Pb) e guardar na linha da vez e na coluna 5 udando a razão de solubilidade que esta na linha da vez e na coluna 3

# Massa Específica do Óleo
para  i  no  intervalo ( 0 , len ( Pvec )):
    se  P  >  Pb :
        rho_ob [ i ] = ( 62.4  *  do  +  0.0136  *  rsb [ i , 3 ] *  dg ) /  bob [ i ]    # usamos rsb e bob, pois são a razão de solubilidade e o fator volume formação do óleo na pressão de bolhas calculadas anteriormente . Vai calcular a massa específica na pressão de bolha para a linha da vez usando a razão de solubilidade e o fator volume formação na pressão de bolha que estão na linha da vez e nas colunas 3 e 5, respectivamente
        rho_o [ i , 6 ] =  rho_ob [ i ] *  np . exp ( co  * ([ i , 1 ] -  Pb ))    # vai calcular a massa específica (p/ P>Pb) e guardar na linha da vez e na coluna 6
    elif  P  <=  Pb :
        rho_ [ i , 6 ] = ( 62.4  *  do  +  0.0136  *  rs [ i , 3 ] *  dg ) /  bo [ i , 5 ]    # vai calcular a massa específica (p/ P<=Pb) e guardar na linha da vez e coluna 6 usando a razão de solubilidade e fato volume formação que estão na linha da vez e nas colunas 3 e 5, respectivamente

# Viscosidade do Óleo Morto
a_uod  =  10  ** ( 0.43  +  8.33  /  API )    # vai calcular o parâmetro a
uod  =  0.32  + ( 1.8  *  10  *  7  /  API  *  4.53 ) * (( 360  /  T  -  260 ) **  a_uod )   # T em Rankine # vai calcular a absorção do óleo morto

# Viscosidade do Óleo Saturado
para  i  no  intervalo (, 0  len ( Pvec )):
    # P <= Pb
    a_uob [ i ] =  10  ** ( - 7.4  * ( 10  **  - 4 ) *  rs [ i , 3 ] +  2.2  * ( 10  **  - 7 ) *  rs [ i , 3 ] **  2 )    # vamos usar rs ou rsb????, vai calcular o parâmetro a da linha da vez usando a razão de solubilidade que esta na linha da vez e na coluna 3
    b_uob [ i ] =  0.68  / ( 10  ** ( 8.62  *  10  **  - 5 ) *  rs [ i , 3 ]) +  0.25  / ( 10  ** ( 1.1  * ( 10  **  - 3 ) *  rs [ i , 3 ]) +  0.062  / ( 10  ** ( 3.74  *  10 **  - 3 ) *  rs [ i , 3 ])    # vai calcular o parâmetro b da linha da vez usando a razão de solubilidade que esta na linha da vez e na coluna 3

    uob [ i , 7 ] =  a_uob [ i ] *  uod  **  b_uob [ i ]    # vai calcular a trajetória do óleo saturado (p/ P<=Pb) e salvar na linha da vez e coluna 7

# Viscosidade do Óleo Sub-Saturado
para  i  no  intervalo ( 0 , len ( Pvec )):
    # P >= Pb
    uo [ i , 8 ] =  uob [ i , 7 ] + ( 0.001  * ( P [ i , 1 ] -  Pb )) * ( 0.024  * ( uob [ i , 7 ] **  1.6 ) +  0.038  * ( uob [ i , 7 ] **  0.56 ))   # vai calcular a subida do óleo sub-saturado (p/ P>=Pb) e guardar na linha da vez e coluna 8 usando a tomada do óleo saturado que esta na linha da vez e coluna 7

# ------------------------Fase Gás---------------------- -#

# Fator de Compressibilidade Isotérmica
para  i  no  intervalo ( 0 , len ( Pvec )):
    a_z [ i ] =  1.39  * (( Tpr  -  0.92 ) **  1  /  2 ) -  0.36  *  Tpr  -  0.101    # vai calcular o parâmetro a da linha da vez
    b_z [ i ] = ( 0.62  -  0.23  *  Tpr ) *  Ppr  + (( 0.066  / ( Tpr  -  0.86 )) -  0.037 ) *  Ppr  **  2  + ( 0.32  *  Ppr  **  6  / ( 10  ** ( 9  * ( Tpr  -  1 ))))    # vai calcular o parâmetro b da linha da vez
    
    c_z [ i ] =  0.132  -  0.32  *  np . log10 ( Tpr )    # vai calcular o parâmetro c da linha da vez
    d_z [ i ] =  10  ** ( 0.3106  -  0.49  *  Tpr  +  0.1824  *  Tpr  **  2 )    # vai calcular o parâmetro a da linha da vez

    z [ i , 2 ] =  a_z [ i ] + (( 1  -  a_ [ i ]) / ( np . exp ( b_z [ i ]))) +  c_z [ i ] *  Ppr  **  d_z [ i ]    # vai calcular o fator de compressibilidade isotérmica e guardar na linha da vez e coluna 2

# Compressibilidade Isotérmica
para  i  no  intervalo ( 0 , len ( Pvec )):
    dz_dp [ i ] =  1  / ((( 0.62  -  0.23  *  Tpr ) *  Ppr  + ( 0.066  / ( Tpr  -  0.86 ) -  0.37 ) *  Ppr  **  2  + ( 0.32  / ( 10  ** ( 9  *  Tpr  -  9 ) )) * Ppr  **  6  ) * np  .exp ( (((0.62  -  0.23  *  Tpr ) + (( 0.132  / ( Tpr  -  0.86 )) -  0.074 ) *  Ppr ) + ( 1.92  / ( 10  ** ( 9  *  Tpr  -  9 ))) *  Ppr  **  5 ))) + ( 10  ** ( 0.3106  -  0.49  *  Tpr  +  0.1824  *  Tpr  **  2) * ( Ppr  ** ((( 10  ** ( 0.3106  -  0.49  *  Tpr  +  0.1824  *  Tpr  **  2 )) -  1 ) * ( 0.132  -  0.32  *  np . log10 ( Tpr )))))    # vai calcular a derivados da linha da vez
    cpr [ i ] =  1  /  Ppr  -  1  /  z  *  dz_dp [ i ]    # vai calcular o Parmetro cpr da linha da vez

    cg [ i , 3 ] =  cpr [ i ] /  Ppc    # vai calcular a compressibilidade isotérmica e salvar na linha da vez e na coluna 3

# Fator Volume Formação
para  i  no  intervalo ( 0 , len ( Pvec )):
    bg [ i , 4 ] =  14.7  /  60  * (( z [ i , 2 ] *  T ) /  P [ i , 1 ])   # Psc = 14.7 psia e Tsc = 60 F # vai calcular o fator volume formação e guadar na linha da vez e na coluna 4 usando o fator de compressibilidade isotérmica que esta na linha da vez e na coluna 2

# Massa Específica do Gás
para  i  no  intervalo ( 0 , len ( Pvec )):
    rho_g [ i , 5 ] =  P [ i , 1 ] *  Mg  / ( z [ i , 2 ] *  R  *  T )   # T em K # vai calcular a massa específica e guardar na linha da vez e na coluna 5 usando o fator de compressibilidade isotérmica que esta na linha da vez e na coluna 2

# Viscosidade do Gás
para  i  no  intervalo ( 0 , len ( Pvec )):
    x_ug [ i ] =  3.47  + ( 1588  /  T ) +  0.0009  *  Mg   # T em Rankine # vai calular o parâmetro x da linha da vez
    y_ug [ i ] =  1.66378  -  0.04679  *  x_ug [ i ]    # vai calular o parâmetro y da linha da vez
    a_ug [ i ] =  x_ug [ i ] *  rho_g [ i , 5 ] **  y_ug [ i ]    # vai calular o parâmetro a da linha da vez usando a massa específica que esta na linha da vez e na coluna 5
    k_ug [ i ] = ( 0.807  * ( Tpr  **  0.618 ) -  0.357  *  np . exp ( -  0.449  *  Tpr ) +  0.34  *  np . exp ( -  4.058  *  Tpr ) +  0.018 ) / ( 0.9490  * ( Tpc  / (( Mg  **  3 ) * ( Ppc  ** 4 ))) **  1  /  6 )   # # T em Rankine, vai calcular o parâmetro k da linha da vez

    ug [ i , 6 ] =  10  **  -  4  *  k_ug [ i ] *  np . exp ( a_ug [ i ])    # vai calcular a subida do gás e guardar na linha da vez e na coluna 6

# ------------------------Fase Água---------------------- -#

# Razão de Solubilidade e salmoura rsw????
ao_rsw  = ( 8.15839 )
a1_rsw  = (− 6.12265  * ( 10  **  -  2 ))
a2_rsw  = ( 1.91663  * ( 10  ** − 4 ))
a3_rsw  = (− 2.1654  * ( 10  ** − 7 ) )

b0_rsw  = ( 1.01021  * ( 10  ** − 2 ))
b1_rsw  = (− 7.44241  * ( 10  ** − 5 ) )
b2_rsw  = ( 3.05553  * ( 10  ** − 7 ))
b3_rsw  = (− 2.94883  * ( 10  ** − 10 ))

c0_rsw  = (- 9.02505 )
c1_rsw  = ( 0.130237 )
c2_rsw  = (− 8.53425  * ( 10  ** − 4 ))
c3_rsw  = ( 2.34122  * ( 10  ** − 6 ))
c4_rsw  = (− 2.37049  * ( 10  ** − 9 ))

a_rsw  =  a0_rsw  +  a1_rsw  *  T  +  a2_rsw  *  T  *  2  +  a3_rsw  *  T  *  3
b_rsw  =  b0_rsw  +  b1_rsw  *  T  +  b2_rsw  *  T  *  2  +  b3_rsw  *  T  *  3
c_rsw  = ( c0_rsw  +  c1_rsw  *  T  +  c2_rsw  *  T  *  2  +  c3_rsw  *  T3  +  c4_rsw  *  T4 ) *  10  *  - 7   # T em F

para  i  em  range90 , len ( Pvec )):
    rsw [ i , 2 ] =  a_rsw  +  b_rsw  *  P [ i , 1 ] +  c_rsw  *  P [ i , 1 ] **  2    # vai calcular a razão de compressibilidade e guardar na linha da vez e na coluna 2

# Compressibilidade Isotérmica
a1_cw  =  7.033
a2_cw  =  0.5415
a3_cw  =  - 537.0
a4_cw  =  403.3

para  i  no  intervalo ( 0 , len ( Pvev )):
    cw [ i , 3 ] =  1  / ( a1_cw  *  P [ i , 1 ] +  a2_cw  *  S  +  a3_cw  *  T  +  a4_cw )   # T em F, vai calcular a compressibilidade isotérmica e guardar na linha da vez e na coluna 3

# Fator Volume Formação
para  i  no  intervalo ( 0 , len ( Pvec )):
    Vwt [ i ] = ( - 1.0001  *  10  **  - 2 ) + ( 1.33391  *  10  **  - 4 ) *  T  + ( 5.50654  *  10  **  - 7 ) *  T  **  2    # vai calular o parêmtro vwt da linha da vez
    Vwp [ i ] = ( - 1.95301  *  10  **  - 9 ) *  P [ i , 1 ] *  T  - ( 1.72834  *  10  **  - 13 ) * ( P [ i , 1 ] **  2 ) *  T  - ( 3.58922  *  10  **  - 7 ) *  P [ i, 1 ] - ( 2.25341  *  10  **  - 10 ) *  P [ i , 1 ] **  2   # T em F, vai calcular o parâmetro vwp da linha da vez

    bw [ i , 4 ] = ( 1  +  Vwt [ i ]) * ( 1  +  Vwp [ i ])    # vai calcular o fator volume formação e guardar na linha da vez e na coluna 4

# Massa Específica da Água onde vamos guardar??????

pw  =  62.368  +  0.438603  *  S  + ( 1.60074  *  10  **  - 3 ) *  S  **  2

# Viscosidade da Água
a0_uw1  = ( 109.527 )
a1_uw1  = (- 8.40564 )
a2_uw1  = ( 0.313314 )
a3_uw1  = ( 8.72213  * ( 10  ** − 3 ))

b0_uw1  = (- 1.12166 )
b1_uw1  = ( 2.63951  * ( 10  ** − 2 ))
b2_uw1  = (− 6.79461  * ( 10  ** − 4 ))
b3_uw1  = (− 5.47119  * ( 10  ** − 5 ))
b4_uw1  = (− 1.55586  * ( 10  ** − 6 ))

a_uw1  =  a0_uw1  +  a1_uw1  *  S  +  a2_uw1  *  S  **  2  +  a3_uw1  *  S  **  3
b_uw1  =  b0_uw1  +  b1_uw1  *  S  +  b2_uw1  *  S  **  2  +  b3_uw1  *  S  **  3  +  b4_uw1  *  S  **  4

uw1  =  a_uw1  *  T  **  b_uw1   # T em F

para  i  em  range90 , len ( Pvec )):
    uw [ i , 6 ] =  uw1  * ( 0.9994  + ( 4.0295  *  10  **  - 5 ) *  P [ i , 1 ] + ( 3.1062  *  10  **  - 9 ) *  P [ i , 1 ] *  2 )    # vai calcular a tomada da água e guardar na linha da vez e na coluna 6
