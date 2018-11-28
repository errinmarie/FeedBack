import React, { Component } from 'react';
import './SingleBlogPost.css';

import { blogPosts } from '../Blog/blogposts.js';

// Get the Article component
import Article from '../../Article/Article.js';

class SingleBlogPost extends Component {
  render() {
    // this needs updating!
    console.log('rendering single blog post', this.props.match.params);
    return (
      <div className="SingleBlogPost">
        <p>Debug: params data coming in as: {this.props.match.params.articleId}</p>

        <Article title={"placeholder"} image={"test"}>
          <p>todo...</p>
        </Article>
      </div>
    );
  }
}

export default SingleBlogPost;
