import React, { Component } from 'react';
import { BrowserRouter as Router } from "react-router-dom";
import '../App.css';
import Header from './Header';
import Content from './Content';
import { Route, Switch } from "react-router-dom";
import Nav from "./Nav";
import LoginForm from './LoginForm';
import SignUpForm from './SignUpForm';
import { connect } from 'react-redux';
import { tokenAuthentication } from '../actions/articlesActions'


class App extends Component {
    constructor(props) {
        super(props);
    }
    componentDidMount() {
        this.props.checkValidToken()
    }
    render() {
        return (
            <Router>
                <div className="container">
                    <Header />
                    <Nav />
                    <Switch>
                        <Route exact path="/" component={Content} />
                        <Route path="/login" component={LoginForm} />
                        <Route path="/signup" component={SignUpForm} />
                        <Route path="/category/:id" component={Content} />
                    </Switch>
                    <div className='footer-section'>
                        Made with <span>&#9829;</span> in <a href='https://altcampus.io/'>altCAMPUS</a>
                </div>
                </div>
            </Router>
        );
    }
}

const mapStateToProps = (state) => {
    return {
        token: state.token,
        isAuthenticated: state.isAuthenticated,
        username: state.username,
    }
}

const mapDispatchToProps = (dispatch) => {
    return {
        checkValidToken: () => dispatch(tokenAuthentication()),
    }
}

App = connect(mapStateToProps, mapDispatchToProps)(App);
export default App;
