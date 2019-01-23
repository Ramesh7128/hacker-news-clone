import React, { Component } from 'react';
import './App.css';
import Header from './Header';
import Search from './Search';
import Content from './Content';
import Footer from './Footer';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      articles: [],
      prevLink: '',
      nextLink: '',
      startIndex: '',
      endIndex: '',
      articleCount: 0,
      searchArticles: [],
      isLoaded: false,
    }
    this.handleArticleSearch = this.handleArticleSearch.bind(this);
    this.handleTopArticleClick = this.handleTopArticleClick.bind(this);
    this.handleMoreArticlesClick = this.handleMoreArticlesClick.bind(this);
  }

  handleArticleSearch(SearchString) {
    const articles = this.state.articles;
    const article = articles.filter(article => article.title === SearchString);
    this.setState(state => ({
      searchArticles: article
    }));
  }

  handleTopArticleClick() {
    this.fetchArticles();
  }

  handleMoreArticlesClick() {
    this.fetchArticles(this.state.nextLink);
  }

  fetchArticles(url='/api/stories/') {
    let base_url = window.location.origin;
    // let base_url = 'http://127.0.0.1:8000';
    url = base_url + url;
    console.log(url);
    console.log(url);
    fetch(url)
      .then(response => {
        return response.json()})
      .then(
        (data) => {
          this.setState((state, props) => ({
            articles: data['data'],
            startIndex: data['startIndex'],
            endIndex: data['endIndex'],
            nextLink: data['nextlink'],
            articleCount: data['count'],
            prevlink: data['prevLink'],
            searchArticles: [],
            isLoaded: true}));
        }
      ) 
  }

  componentDidMount() {
    this.fetchArticles();
  }

  render() {
    console.log(this.state.nextLink);
    return (
      <div className="container">
        <Header handleTopArticleClick={this.handleTopArticleClick} />
        <Search handleArticleSearch={this.handleArticleSearch} articles={this.state.articles} />
        <Content article={this.state} />
        <Footer handleMoreArticlesClick={this.handleMoreArticlesClick}/>
      </div>
    );
  }
}

export default App;
