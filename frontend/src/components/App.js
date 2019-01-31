import React, { Component } from 'react';
import '../App.css';
import Header from '../containers/Header';
// import Search from './Search';
import Content from '../containers/Content';
import Footer from '../containers/Footer';

class App extends Component {
  render() {
    return (
      <div className="container">
        <Header />
        {/* <Search handleArticleSearch={this.handleArticleSearch} articles={store.getState().articles} /> */}
        <Content />
        <Footer />
      </div>
    );
  }
}

export default App;
