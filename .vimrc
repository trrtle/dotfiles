" Plugins
call plug#begin('~/.vim/plugged')
Plug 'ctrlpvim/ctrlp.vim'
Plug 'mbbill/undotree'
Plug 'morhetz/gruvbox'
Plug 'preservim/nerdtree'
Plug 'tpope/vim-fugitive'
Plug 'Valloric/YouCompleteMe'
Plug 'vim-scripts/indentpython.vim' 
Plug 'vim-utils/vim-man'
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
set nowrap
set noswapfile
set nobackup
set undodir=~/.vim/undodir
set undofile
set incsearch

" PEP 8 python
set encoding=utf-8
set tabstop=4 softtabstop=4
set shiftwidth=4
set textwidth=79
set autoindent
set fileformat=unix

" configuration
nnoremap <SPACE> <Nop>
let mapleader = " "
let g:ctrlp_user_command = ['.git/', 'git --git-dir=%s/.git ls-files -oc --exclude-standard']

map <leader>g  :YcmCompleter GoToDefinitionElseDeclaration<CR>
nnoremap <leader>gt :YcmCompleter GoTo<CR>
nnoremap <leader>gr :YcmCompleter GoToReferences<CR>

nnoremap <leader>h :wincmd h<CR>
nnoremap <leader>j :wincmd j<CR>
nnoremap <leader>k :wincmd k<CR>
nnoremap <leader>l :wincmd l<CR>
nnoremap <leader>v :vsplit <CR>
nnoremap <Leader>+ :vertical resize +5<CR>
nnoremap <Leader>- :vertical resize -5<CR>--

map <leader>t :NERDTreeToggle<CR>
map <C-l> :tabn<CR>
map <C-h> :tabp<CR>
map <C-n> :tabnew<CR>
