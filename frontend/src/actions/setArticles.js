import axios from 'axios';

const fetchArticles = url => {
    // let base_url = window.location.origin;
    let base_url = 'http://127.0.0.1:8000';
    url = base_url + url;
    console.log(url);
    console.log(url);
    fetch(url)
        .then(response => {
            return response.json()
        })
        .then(
            (data) => ({
                type: "fetch_articles",
                payload: {
                    articles: data['data'],
                    startIndex: data['startIndex'],
                    endIndex: data['endIndex'],
                    nextLink: data['nextlink'],
                    articleCount: data['count'],
                    prevlink: data['prevLink'],
                    searchArticles: [],
                    isLoaded: true
                }
            }));
}