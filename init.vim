" Plugins
call plug#begin('~/.vim/plugged')
Plug 'morhetz/gruvbox'
call plug#end()

" Configuration
set nu
set noswapfile
set nobackup
set undodir=~/.config/nvim/undodir
set undofile
nnoremap <SPACE> <Nop>
let mapleader = " "


" syntax highlighting
syntax on
colorscheme gruvbox
set background=dark
set colorcolumn=100
highlight ColorColumn ctermbg=lightgrey

" PEP 8 Python
set encoding=utf-8
set autoindent
set tabstop=2 softtabstop=2
set shiftwidth=2
set fileformat=unix

