import axios from 'axios';

export const FETCH_PRODUCTS_BEGIN = 'FETCH_PRODUCTS_BEGIN';
export const FETCH_PRODUCTS_SUCCESS = 'FETCH_PRODUCTS_SUCCESS';
export const FETCH_PRODUCTS_FAILURE = 'FETCH_PRODUCTS_FAILURE';


export function fetchArticles(url='/api/stories/') {
    // let base_url = window.location.origin;
    let base_url = 'http://127.0.0.1:8000';
    url = base_url + url;
    return function (dispatch) {
        dispatch({ type: FETCH_PRODUCTS_BEGIN });
        axios.get(url)
            .then((response) => {
                dispatch({ type: FETCH_PRODUCTS_SUCCESS, payload: response.data })
            })
            .catch((error) => {
                dispatch({ type: FETCH_PRODUCTS_FAILURE, payload: error });
            })
    }
}
