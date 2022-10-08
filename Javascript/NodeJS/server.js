const express = require('express') // Importação padrão
const app = express() // Cria um app variable para a aplicação

app.use(express.static("public")) // Serve static files. Nesse caso para o diretorio 'root/public'
app.use(express.urlencoded({ extended: true})) // Permite acessar informações vindas de forms. req.body.firstName por ex. Extended true para evitar warnings.
app.use(express.json()) // Mesma coisa do urlencoded acima, mas para Json requests.

app.set('view engine', 'ejs')// View engine. Podemus usar ejs, pug, etc.

app.use(logger)

app.get('/', logger, (req, res) => {// Tipo de rota. 
  console.log('Here')

  // res.send('Hi') // Informação para ser enviada para o servidor pela função
  // res.status(500).send('Hi')//Status especifico. Consultar referencia: https://expressjs.com/en/5x/api.html#res.sendStatus
  // res.json({ message: "Mensagem"})        // Direto, sem ser especifico.
  // res.status(500).json({message: "Error"})// Mais específico.
  // res.download("server.js")               // https://www.geeksforgeeks.org/express-js-res-download-function/
  res.render('index', {text: 'Hello, World!'}) // renderiza HTML. No caso root/views/index.ejs
})

const userRouter = require('./routes/users') // Importando router encapsulado

app.use('/users', userRouter) // Avisa para utilizar o router. Nome da rota em URL + função encapsulada

function logger(req, res, next){ // App.use acima. Podemos colocar quantos middlewares quisermos ali dentro, root/server.js: 
  console.log(req.originalUrl) // Vai printar a url atual.                     
  next() // Middlewares precisam de next. Agora podemos aplicar a function middleware logger dentro de funções
} // Também podemos colocar isso no root/routes/users.js da mesma forma.

app.listen(3000)//Port to server de testes


