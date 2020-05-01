" Plugins
call plug#begin('~/.vim/plugged')
Plug 'vim-scripts/indentpython.vim' 
Plug 'Valloric/YouCompleteMe'
Plug 'morhetz/gruvbox'
Plug 'preservim/nerdtree'
call plug#end()

" allow copy and pasting from other sources
vnoremap <C-c> "+y
map <C-v> "+p

" syntax highlighting
let python_highlight_all=1
syntax on
colorscheme gruvbox
set background=dark

set noerrorbells
set expandtab
set smartindent
set nu
"set nowrap
set noswapfile
set nobackup
set undodir=~/.vim/undodir
set undofile
set incsearch
set encoding=utf-8

let mapleader = " "
map <leader>g  :YcmCompleter GoToDefinitionElseDeclaration<CR>
map <C-n> :NERDTreeToggle<CR>

" PEP 8 python
set tabstop=4 softtabstop=4
set shiftwidth=4
set textwidth=79
set autoindent
set fileformat=unix

