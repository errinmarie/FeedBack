import React, { Component } from 'react';
import './Blog.css';
import { blogPosts } from './blogposts.js';

// Get the Article component
import Article from '../../Article/Article.js';

class Blog extends Component {
  render() {
    return (
      <div className="Blog">
        <h1>Blog</h1>
        {
          blogPosts.map((post, index) => (
            <Article title={post.title} image={post.image} key={index}>
              {
                post.content.map((text, index) => (
                  <p key={index}>{text}</p>
                ))
              }
            </Article>
          ))
        }
      </div>
    );
  }
}

export default Blog;