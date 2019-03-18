import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import { connect } from 'react-redux';
import { authLogout } from '../actions/articlesActions';
import { withRouter } from 'react-router-dom';

class Login extends Component {
    constructor(props) {
        super(props);
        this.handleLogout = this.handleLogout.bind(this);
    }

    handleLogout(event) {
        this.props.logout();
        this.props.history.push('/');
    }

    render() {
        return (
            <div>
                {this.props.isAuthenticated ?
                    <ul>
                        <li className="login-btn" onClick={this.handleLogout}>
                            <div className='userlogincreds'>
                                <div className='login-username'>
                                    {this.props.username}
                                </div>
                                <div className='logout-btn'>
                                    Logout
                                </div>
                            </div>
                        </li>
                    </ul>
                    :
                    <ul>
                        <li>
                            <Link to="/login"><div className='login-btn'>Login</div></Link>
                        </li>
                    </ul>
                }
            </div>
        )
    }
}

const mapDispatchToProps = (dispatch, ownProps) => {
    return {
        logout: () => dispatch(authLogout())
    }
}

const mapStateToProps = (state) => {
    return {
        isAuthenticated: state.isAuthenticated,
        username: state.username
    }
}

Login = connect(mapStateToProps, mapDispatchToProps)(Login)
export default withRouter(Login);