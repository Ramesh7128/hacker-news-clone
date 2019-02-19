import axios from 'axios';

export const FETCH_STORIES_BEGIN = 'FETCH_STORIES_BEGIN';
export const FETCH_STORIES_SUCCESS = 'FETCH_STORIES_SUCCESS';
export const FETCH_STORIES_FAILURE = 'FETCH_STORIES_FAILURE';

export const FETCH_SEARCH_STORIES_BEGIN = 'FETCH_SEARCH_STORIES_BEGIN';
export const FETCH_SEARCH_STORIES_SUCCESS = 'FETCH_SEARCH_STORIES_SUCCESS';
export const FETCH_SEARCH_STORIES_FAILURE = 'FETCH_SEARCH_STORIES_FAILURE';


export function fetchArticles(url='/api/stories/') {
    // let base_url = window.location.origin;
    let base_url = 'http://127.0.0.1:8000';
    url = base_url + url;
    return function (dispatch) {
        dispatch({ type: FETCH_STORIES_BEGIN });
        axios.get(url)
            .then((response) => {
                dispatch({ type: FETCH_STORIES_SUCCESS, payload: response.data })
            })
            .catch((error) => {
                dispatch({ type: FETCH_STORIES_FAILURE, payload: error });
            })
    }
}

export function fetchSearchArticles(query='') {
    // let base_url = window.location.origin
    let base_url = 'http://127.0.0.1:8000';
    let url = base_url + '/api/articles_search/?q=' + query
    return function (dispatch) {
        dispatch({type: FETCH_SEARCH_STORIES_BEGIN});
        axios.get(url)
            .then((response) => {
                dispatch({type: FETCH_SEARCH_STORIES_SUCCESS, payload: response.data})
            })
            .catch((error) => {
                dispatch({ type: FETCH_SEARCH_STORIES_FAILURE, payload: error});
            })
    }
}
