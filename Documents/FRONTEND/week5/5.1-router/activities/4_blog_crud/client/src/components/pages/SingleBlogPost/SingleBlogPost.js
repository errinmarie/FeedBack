import React, { Component } from 'react';
import './SingleBlogPost.css';

// Get the Article component
import Article from '../../Article/Article.js';

class SingleBlogPost extends Component {
  state = {
    post: null,
  }

  componentDidMount() {
    console.log('need to load', this.props.match.params.index);
    // e.g. /api/2


    // Modify this...
    fetch('/api/')
      .then(response => response.json())
      .then(data => {
        console.log('got data back!', data);

        // Do something...
      });
  }


  render() {
    const post = this.state.post;
    return (
      <div className="SingleBlogPost">
        <h1>Single Post</h1>
        {
          post ? (
            <Article title={post.title} image={post.image}>
              {
                post.content.map((text, index) => (
                  <p key={index}>{text}</p>
                ))
              }
            </Article>
          ) : null
        }

      </div>
    );
  }
}

export default SingleBlogPost;
