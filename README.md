# Latam News Dashboard
Dashboard de noticias de Latinoamerica

[![npm Version][NPM VERSION BADGE]][NPM PAGE]
[![Node.js][NODE VERSION BADGE]][NODE PAGE]
[![python](https://img.shields.io/badge/Python-3.9-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)

## Acerca del proyecto
<p align="center">
  <img src="https://github.com/TawsEspol/DashBoardWeb-PreTaws/assets/10170032/cad1a021-58dd-4df8-bc50-a631300b2ade" />
</p>
El proyecto consiste en un dashboard exploratorio de noticias en tres países de latinoamérica: 🇪🇨 Ecuador, 🇲🇽 México y 🇻🇪 Venezuela. 
En este se analizan categorías de crimen, política, corrupción, salud, religión, desempleo, educación, economía, y deportes.
Para ello se hace uso de cuatro tipos de gráficos, siendo estos de barra, radar, timeseries y wordclouds.

### Alcances
- **Top Publicaciones**: Al inicio se conoce el país, el mes y el año con mayor cantidad de publicaciones. Esto permite entender en cuál de los criterios pudo haber existido una noticia con especial cobertura.
- **Navegación entre charts**: Disponen de charts con el fin de determinar insights,
  - **Sentiment Analysis (Bar)**, conocer si la perspectiva dentro de un país ante los sucesos es positiva, neutra o negativa; a partir categorías.
  - **Trending topics (Radar y TimeSeries)**, conocer que categorías guardan mayor relevancia dentro de un país en función del año (de 2015 a 2018); en dos formatos gráficos distintos.
  - **Main titles (Wordcloud)**, conocer que palabras se repiten con mayor frecuencia en las noticias dentro de un país.
 
<p align="center">
  <img src="https://github.com/TawsEspol/DashBoardWeb-PreTaws/assets/10170032/c55e2d20-3ba3-426b-93a3-7486528e9080" />
</p>

## ¿Cómo empezar?

1. En consola ubicarse en el directorio del proyecto web `./vuetify/`.
2. Instalar dependencias mediante `npm install`.
3. Implementar configuraciones mediante export `NODE_OPTIONS=--openssl-legacy-provider`-
4. Desplegar el servidor local `npm run serve`.



[NPM VERSION BADGE]: https://img.shields.io/npm/v/readme-md.svg
[NPM PAGE]: https://www.npmjs.com/package/readme-md
[NODE VERSION BADGE]: https://img.shields.io/node/v/readme-md.svg
[NODE PAGE]: https://nodejs.org/
