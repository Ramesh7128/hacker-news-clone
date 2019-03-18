import axios from 'axios';

export const FETCH_STORIES_BEGIN = 'FETCH_STORIES_BEGIN';
export const FETCH_STORIES_SUCCESS = 'FETCH_STORIES_SUCCESS';
export const FETCH_STORIES_FAILURE = 'FETCH_STORIES_FAILURE';

export const FETCH_SEARCH_STORIES_BEGIN = 'FETCH_SEARCH_STORIES_BEGIN';
export const FETCH_SEARCH_STORIES_SUCCESS = 'FETCH_SEARCH_STORIES_SUCCESS';
export const FETCH_SEARCH_STORIES_FAILURE = 'FETCH_SEARCH_STORIES_FAILURE';
export const CONTENT_PAGE_RERENDER = 'CONTENT_PAGE_RERENDER';

export const AUTH_START = 'AUTH_START';
export const AUTH_SUCCESS = 'AUTH_SUCESS';
export const AUTH_FAIL = 'AUTH_FAIL';
export const AUTH_LOGOUT = 'AUTH_LOGOUT';



export function fetchArticles(url = '/api/stories/') {
    // let base_url = window.location.origin;
    let token = localStorage.getItem('token', '');
    let base_url = 'http://127.0.0.1:8000';
    url = base_url + url;
    return function (dispatch) {
        dispatch({ type: FETCH_STORIES_BEGIN });
        axios.get(url, token && { headers: { Authorization: `Token ${token}` } })
            .then((response) => {
                console.log(response.data);
                dispatch({ type: FETCH_STORIES_SUCCESS, payload: response.data })
            })
            .catch((error) => {
                dispatch({ type: FETCH_STORIES_FAILURE, payload: error });
            })
    }
}

export function fetchSearchArticles(query = '', token = '') {
    // let base_url = window.location.origin
    let base_url = 'http://127.0.0.1:8000';
    let url = base_url + '/api/articles_search/?q=' + query
    return function (dispatch) {
        dispatch({ type: FETCH_SEARCH_STORIES_BEGIN });
        axios.get(url, { headers: { Authorization: `Token ${token}` } })
            .then((response) => {
                dispatch({ type: FETCH_SEARCH_STORIES_SUCCESS, payload: response.data })
            })
            .catch((error) => {
                dispatch({ type: FETCH_SEARCH_STORIES_FAILURE, payload: error });
            })
    }
}

export const authStart = () => {
    return {
        type: AUTH_START
    }
}

export const authSuccess = (token, username) => {
    return {
        type: AUTH_SUCCESS,
        token: token,
        username: username
    }
}

export const authFail = error => {
    return {
        type: AUTH_FAIL,
        error: error
    }
}

export const authLogout = () => {
    localStorage.removeItem('token');
    return {
        type: AUTH_LOGOUT
    }
}

export const authLogin = (email, password) => {
    return dispatch => {
        dispatch(authStart());
        axios.post('http://127.0.0.1:8000/api/users/login', {
            "user": {
                "email": email,
                "password": password
            }
        })
            .then((res) => {
                const token = res.data.user.token;
                const username = res.data.user.username;
                localStorage.setItem('token', token);
                dispatch(authSuccess(token, username));
            })
            .catch((error) => {
                localStorage.removeItem('token');
                dispatch(authFail(error.response.data.user.error.error));
            });
    }
}

export const authSignUp = (email, username, password) => {
    return dispatch => {
        dispatch(authStart());
        axios.post('http://127.0.0.1:8000/api/users/', {
            "user": {
                "email": email,
                "username": username,
                "password": password
            }
        })
            .then(res => {
                const token = res.data.user.token;
                const username = res.data.user.username
                localStorage.setItem('token', token);
                dispatch(authSuccess(token, username));
            })
            .catch((error) => {
                console.log(error.response.data);
                localStorage.removeItem('token');
                dispatch(authFail(error.response.data.user.error));
            });
    }
}

export const tokenAuthentication = () => {

    return dispatch => {
        const token = localStorage.getItem('token');
        if (token == undefined) {
            dispatch(authLogout());
        } else {
            axios.get('http://127.0.0.1:8000/api/user', { headers: { Authorization: `Token ${token}` } })
                .then(res => {
                    if (res.status == 200) {
                        console.log(res.data);
                        const username = res.data.user.username;
                        dispatch(authSuccess(token, username));
                    }
                }).catch((error) => {
                    localStorage.removeItem('token');
                    dispatch(authFail(error.response.data.user.error));
                });
        }
    }
}


export const starArticles = (articleID) => {
    const token = localStorage.getItem('token');
    if (token == undefined) {
        token = ''
    }
    axios.post('http://127.0.0.1:8000/api/starred', {
        'articleID': articleID
    }, { headers: { Authorization: `Token ${token}` } });
}
