check_repo() {
  local REPO_DIR="$HOME/AmazingGroup"
  cd "$REPO_DIR" || return

  git fetch --all --quiet 2>/dev/null

  local LOCAL
  local REMOTE
  LOCAL=$(git rev-parse main 2>/dev/null)
  REMOTE=$(git rev-parse origin/main 2>/dev/null)

  if [ "$LOCAL" != "$REMOTE" ]; then
    echo "⚠️  Il main ha aggiornamenti non mergiati nel tuo branch."
    echo "   Commit in arrivo:"
    git log --oneline main..origin/main
    echo ""
    read -rp "   Vuoi mergiare ora? (s/n): " RISPOSTA
    if [ "$RISPOSTA" = "s" ]; then
      git merge origin/main
      echo "✅ Merge completato."
    else
      echo "⏭️  Merge rimandato."
    fi
  else
    echo "✅ Main aggiornato — nessuna azione richiesta."
  fi

  echo ""
  echo "📂 Apro AmazingGroup in VS Code..."
  code "$REPO_DIR"

  cd "$HOME"
}

check_repo
