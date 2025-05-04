# EDA Receita Federal

### Exploração do conjunto de dados
<p>O conjunto de dados consiste em 5 tabelas que possuem informações referentes as arrecadações de impostos e contribuições federais, são elas:</p>
<ol>
    <li>Arrecadação por Estado</li>
    <li>Arrecadação por CNAE</li>
    <li>Arrecadação de IR e IPI</li>
    <li>Arrecadação de ITR</li>
    <li>Arrecadação por Natureza Jurídica</li>
</ol>

### Estrutura das tabelas
<h4><u>Arrecadação por Estado</u></h4>
<p>A tabela de arrecadação por estado abrange dados de janeiro de 2000 até agosto de 2024 e possui os valores de impostos arrecadados por ano, mês e UF</p>

<h4><u>Arrecadação por CNAE</u></h4>
<p>A tabela de arrecadação por CNAE abrange dados de janeiro de 2016 até agosto de 2024 e possui os valores de impostos arrecadados por ano, mes e código da seção da atividade econômica.</p>

<h4><u>Arrecadação de IR e IPI</u></h4>
<p>A tabela de arrecadação de IR e IPI abrange dados de janeiro de 2019 até agosto de 2024 e possui os valores de de IR e IPI arrecados em cada mês de cada um dos anos</p>

<h4><u>Arrecadação de ITR</u></h4>
<p>A tabela de arrecadação de ITR abrange dados de janeiro de 2017 até agosto de 2024 e possui os valores de ITR (Imposto sobre a Propriedade Territorial Rural) arrecadados em cada mês de cada um dos anos e agrupados também por UF.</p>

<h4><u>Arrecadação por Natureza Jurídica</u></h4>
<p>A tabela de arrecação por Natureza Jurídica abrange dados de janeiro de 2016 até agosto de 2024 e possui os valores de impostos arrecadados em cada mês de cada ano agrupado pelo código de natureza jurídica.</p>

<h2>Sobre o projeto</h2>

### Extração dos dados
<p>Para realizar a extração dos dados, optei por criar um simples extrator python que conecta ao banco de dados BigQuery e puxa a informação completa de todas as tabelas para arquivos csv, localizados dentro da pasta <b>dados_brutos</b>.</p>

<p>Outra maneira com a qual podemos realizar a extração desses dados é criar um web scraping para realizar o download do arquivo compactado, após esse processo, é ncessário descompactar o arquivo, e então o tratamento seguiria da mesma maneira, pois ambas as formas trabalharão com o arquivo csv, lembrando que o web scraping seria apenas para deixar o processo automatizado, já que o download pode ser realizado também de forma manual, o que torna o processo menos dinâmico.</p>

### Limpeza dos dados
<p>Para o processo de limpeza dos dados optei por realizar a substituição dos valores não numéricos por 0, juntamente com a padronização das datas para o padrão yyyy-MM-dd o que posteriormente facilitará análises temporais, além disso na tabela de arrecadação de IR e IPI separei o número do dicendio, caso futuramente seja idealizado análises que pretendam realizar o levantamento por impostos.</p>

### Insights e KPIs
<ul>
    <li>Através dos dados de arrecadação de ITR é possível fazer um levantamento da evolução da arrecadação nos munícipios de atividade da vinícola como Canela e Gramado.</li>
    <li>Comparar e acompanhar os estados que possuem os maiores valores de arrecadação de impostos sobre a produção de bebidas, entender onde o mercado está mais aquecido e com maior número de competidores.</li>
    <li>Através da seção C da tabela de arrecadação por CNAE é possível analisar também a distribuição de impostos para o CNAE de distribuição de bebidas, o objetio aqui seria compreender quais impostos representam maior valor.</li>
</ul>