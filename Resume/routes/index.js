var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { 
    title: 'My Resume' });
});

/* GET about me page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'About' });
});

/* GET video of me page. */
router.get('/video', function(req, res, next) {
  res.render('index', { title: 'Video about me' });
});

/* GET projects page. */
router.get('/projects', function(req, res, next) {
  res.render('index', { title: 'Projects' });
});

/* GET contact page. */
router.get('/contact', function(req, res, next) {
  res.render('index', { title: 'Contact Me' });
});
module.exports = router;
