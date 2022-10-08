const express = require('express')
const router = express.Router() // Router eh um mini App para rotas independentes, ajuda a encapsular rotas do server.js

router.get('/', (req, res) => { // Rota para users. localhost/users
  console.log(req.query.name) // EX: localhost/users/?name=Gabriel, a partir do ? ..
  res.send('User List')
})

router.get('/new', (req, res) => { // Rota para cadastro de users. localhost/users/new
  res.render("users/new", { firstName: "Test"} ) // Diretorio root/views/users/new.ejs. Esse firstname eh apenas para preencher automatico
  // res.send('User New Form')
})

router.post('/', (req, res) => {
  const isValid = true // Validação, caso true, continuar criando o user
  if (isValid) { //
    users.push({ firstName: req.body.firstName }) //users seria a variavel abaixo no fim do codigo "const users = ....". 
    res.redirect(`/users/${users.length - 1}`) //req.body.firstName = form
  } else {
    console.log("Error")
    res.render('users/new', { firstName: req.body.firstName }) // Vai repopular o form automaticamente.
  }
})

router
  .route("/:id")
  .get((req, res) => {// Pega dinâmicamente o ID, aqui é /users/[id]. 
    // req.params.id // Armazenado em req.params.id. Se acima fosse /:userId/, aqui seria req.params.userId
    res.send(`Get User With Id ${req.params.id}`) 
  })
  .put((req, res) => {
    res.send(`Update User With Id ${req.params.id}`) 
  })
  .delete((req, res) => {
    res.send(`Delete User With Id ${req.params.id}`) 
  })

const users = [{ name: "Gabriel"}, { name: "Gabriel2"}]
router.param("id", (req, res, next, id) => { // Qdo achar um param, nosso caso id, vai realizar uma função especifica. No caso puxar nossos 2 usuarios acima. Isso faz possivel acessar esses users em qualquer parte do codigo tbm.
  req.user = users[id] // Automaticamente seta o id se nao tiver implicito.
  // console.log(user)
  next() // quando chamamos a variavel next acima, precisamos colocar aqui também para ele não ficar carregando infinitamente esperando pela proxima função.
})

module.exports = router