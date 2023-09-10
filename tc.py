/*Edited using the Default theme*/

@import url('https://fonts.googleapis.com/css2?family=Source+Sans+Pro:wght@300;400;700&display=swap');

::-webkit-scrollbar {
  width: 8px;
  height: 8px;
  background: #44475a;
}
::-webkit-scrollbar-thumb {
  border-radius: 20px;
  background-color: #bd93f9;
}
body{
  background-color: #2b2d3b;
  font-family: 'Source Sans Pro', sans-serif !important;
}
body.ownlist {
  background-image: url("https://images2.imgbox.com/8e/39/JCxOMUoH_o.png");
}
a {
  color: #f8f8f2;
  text-decoration: none !important;
}
/* Main container */
.list-container{
  border-radius: 20px;
  box-shadow: 3px 3px 4px #00000026;
  margin-bottom: 70px;
  background-color: #22212c;
  border: #514d7c 1px solid;
}
.cover-block .image-container img {
  border-radius: 18px;
}
.cover-block .image-container {
  padding-top: 16px;
  padding-bottom: 16px;
}
.status-menu-container {
  background-color: #423e64;
  display: flex;
  justify-content: center;
  align-items: center;
  box-shadow: 0 0 8px 0px #06060687;
  border-bottom: none;
  clip-path: inset(-48px 0px -55px 0px);
}
.status-menu-container .status-menu {
  display: flex;
}
.status-menu-container .status-menu .status-button {
  padding: 8px 10px;
}
.status-menu-container .status-menu .status-button:hover {
  color: #bd93f9;
}
.status-menu-container .status-menu .status-button:after {
  left: 50%;
  transform: translateX(-50%);
  background-color: #caa9fa;
  width: 5px;
  border-radius: 4em;
  height: 5px;
}
.status-menu-container .status-menu .status-button.on {
  color: #ffffff;
}
.status-menu-container .status-menu .status-button.on:hover {
  color: #caa9fa;
}
.status-menu-container .status-menu .status-button.on:after, .status-menu .status-button:hover:after {
  width: 20px !important;
}
.status-menu-container .search-container #search-box input {
  background: transparent;
  border: solid 2px #8e66c5;
  border-radius: 4px;
  padding: 4px;
  color: #fff;
}
.status-menu-container .search-container #search-box input:focus {
  outline:none;
}
.status-menu-container .search-container #search-box {
  margin-top: 8px;
}
.status-menu-container .search-container #search-button {
  margin-top: 12px;
}
.list-unit .list-status-title {
  background-color: #44475a;
  width: auto;
  border-radius: 20px;
  margin-left: 1rem;
  margin-right: 1rem;
  margin-bottom: 24px;
}
.list-unit .list-status-title .stats {
  margin-right: 1rem;
}
.list-unit .list-status-title .stats a {
  transition: .4s ease-out;
}
.list-unit .list-status-title .stats a:hover {
  color: #8be9fd;
}
.list-unit .list-stats {
  background-color: #bd93f9;
  font-size: 1.2em;
  color: #22212c;
  font-weight: 700;
}
.list-table{
  border: none;
}
.list-table .list-table-header .header-title .link {
  font-size: 12px;
}
.list-table .list-table-header .header-title .link.sort:hover {
  color: #bd93f9;
}
.list-table-data{
  padding: 6px;
  transition: .3s ease-out;
}
.list-table-data:hover {
  background-color: #434156;
}
td.data.number {
  background-color: #37354a;
}
.list-table .list-table-data .data {
  border-bottom: #bd93f9 1px solid;
  color: #fff;
}
.list-table .list-table-data .data.image .image {
  width: auto;
  border: none;
}
.list-table .list-table-data .data.title .link {
  font-size: 1.4em;
}
.list-table .list-table-data .data.title .add-edit-more {
  font-size: 1.1em;
}
.list-table .list-table-data .data.score .link {
  font-size: 1.4em;
}
.list-table>tbody:nth-of-type(2n+1) {
  background-color: inherit;
}
.list-table .list-table-data a {
  transition: .4s ease-out;
}
.icon-add-episode{
  color: #bd93f9;
}
.icon-add-episode:hover{
  color: #bfbfbf !important;
}
.list-table .list-table-data a:not(.edit-disabled):hover {
  color: #bd93f9;
}
.list-table .list-table-data .tags .edit {
  display: inline-block;
  width: auto;
  text-align: center;
  color: #ffffff;
  background-color: #caa9fa;
  padding: .35em .65em;
  font-weight: 700;
  white-space: nowrap;
  vertical-align: baseline;
  border-radius: .375rem;
  line-height: 1.1;
  box-shadow: 2px 2px #fff;
}
.list-table .list-table-data .tags .edit:hover {
  color: #423e64 !important;
  background-color: #8e66c5;
  box-shadow: 0px 0px #423e64;
}
.list-table .list-table-data .data.status.reading, .list-table .list-table-data .data.status.watching {
  background-color: #50fa7b
}
.list-table .list-table-data .data.status.completed {
  background-color: #8be9fd;
}
.list-table .list-table-data .data.status.onhold {
  background-color: #f1fa8c;
}
.list-table .list-table-data .data.status.dropped {
  background-color: #ff6e67;
}
.list-table .list-table-data .data.status.plantoread, .list-table .list-table-data .data.status.plantowatch {
  background-color: #bfbfbf;
}
.icon-watch2 .malicon.malicon-movie-episode, .icon-watch2 .malicon.malicon-movie-pv, .icon-watch2 .malicon.malicon-streaming, .icon-watch-pv2 .malicon.malicon-movie-episode, .icon-watch-pv2 .malicon.malicon-movie-pv, .icon-watch-pv2 .malicon.malicon-streaming {
  color: #bd93f9 !important;
}
/* floating Menu */
.list-menu-float {
  border: none;
  border-radius: 20px;
  background: none;
  left: 4px;
}
.list-menu-float .icon-menu .text {
  top: 16px;
  left: 40px;
}
.list-menu-float .icon-menu:not(.profile):hover {
  background-color: #bd93f9;
}
.list-menu-float .icon-menu.setting:hover .text .link-list-setting, .list-menu-float .icon-menu.setting:hover .text .link-style-setting {
  background-color: #bd93f9;
}
/* settings - floating Menu*/
.list-menu-float .icon-menu.setting svg.icon-setting {
  left: 14px;
  top: 14px;
}
.list-menu-float .icon-menu.setting {
  border-radius: 20px;
  box-shadow: 2px 1px 8px #00000012;
  margin-top: 15px;
}
.list-menu-float .icon-menu.setting:hover .text .link-list-setting {
  border-radius: 0 20px 0 0;
}
.list-menu-float .icon-menu.setting:hover .text .link-list-setting:hover {
  background-color: #8e66c5;
}
.list-menu-float .icon-menu.setting:hover .text .link-style-setting {
  border-top: none;
  border-radius: 0 0 20px 20px;
}
.list-menu-float .icon-menu.setting:hover .text .link-style-setting:hover {
  background-color: #8e66c5;
}
/* logout - floating Menu*/
.list-menu-float .icon-menu.logout svg.icon-logout {
  left: 16px;
  top: 16px;
}
.list-menu-float .icon-menu.logout {
  border-radius: 20px;
  box-shadow: 2px 1px 8px #00000012;
  margin-top: 5px;
}
/* export - floating Menu*/
.list-menu-float .icon-menu.export svg.icon-export {
  left: 14.3px;
  top: 13px;
}
.list-menu-float .icon-menu.export {
  border-radius: 20px;
  box-shadow: 2px 1px 8px #00000012;
  margin-top: 5px;
}
/* history - floating Menu*/
.list-menu-float .icon-menu.history svg.icon-history {
  left: 14px;
  top: 14px;
}
.list-menu-float .icon-menu.history {
  border-radius: 20px;
  box-shadow: 2px 1px 8px #00000012;
  margin-top: 5px;
}
/* manga list - floating Menu*/
.list-menu-float .icon-menu.manga-list svg.icon-manga-list {
  left: 14px;
  top: 13px;
}
.list-menu-float .icon-menu.manga-list {
  border-radius: 20px;
  box-shadow: 2px 1px 8px #00000012;
  margin-top: 5px;
}
/* animelist - floating Menu*/
.list-menu-float .icon-menu.anime-list svg.icon-anime-list {
  left: 14px;
  top: 13px;
}
.list-menu-float .icon-menu.anime-list {
  border-radius: 20px;
  box-shadow: 2px 1px 8px #00000012;
  margin-top: 5px;
}
/* quick add - floating Menu*/
.list-menu-float .icon-menu.quick-add svg.icon-quick-add {
  left: 14px;
  top: 13px;
}
.list-menu-float .icon-menu.quick-add {
  border-radius: 20px;
  box-shadow: 2px 1px 8px #00000012;
  margin-top: 5px;
}
/* profile - floating Menu*/
.list-menu-float .icon-menu.profile {
  border-radius: 20px;
  box-shadow: 2px 1px 8px #00000012;
}
/* footer */
#footer-block {
  box-shadow: -2px -2px 8px #22212c;
  background-color: #383a59;
}
/* filter modal */
#advanced-options {
  background-color: #282a36;
  color: #ffffff;
  border-radius: 20px;
  border: solid 2px #bd93f9;
}
#advanced-options .sort-widget input[type=radio]:checked + label {
  background-color: #bd93f9;
  border: #9654f3 1px solid;
}
#advanced-options .btn-apply{
  background-color: rgb(189 147 249);
  border: solid 1px #9654f3;
}
#advanced-options .btn-apply:hover{
  background-color: rgb(220, 197, 251);
  border: solid 1px rgb(220, 197, 251);
  color: #282a36;
}
#advanced-options .btn-clear {
  background-color: #7c7c7c;
  border: solid 1px #7e7c7c;
  color: #ffffff;
}
#advanced-options .btn-clear:hover {
  background-color: #eeeeee;
  border: solid 1px #bbbbbb;
  color: #282a36;
}
#advanced-options input[type], #advanced-options select {
  border-radius: 4px;
}
#advanced-options input[type]:focus, #advanced-options select:focus {
  outline:none;
  border: solid 2px #bd93f9;
}
/* quick add modal */
#fancybox-outer {
  background-color: #282a36 !important;
  color: #ffffff;
  border-radius: 20px;
  border: solid 2px #bd93f9;
}
#fancybox-frame {
  border-radius: 20px;
}
/*
  Quick Add Modal: Further can not be edited since the content is called by an iframe dynamically
*/
