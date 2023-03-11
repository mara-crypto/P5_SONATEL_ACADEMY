################################################################################
################################################################################
########################Verification Numero Classe #############################
is_valid_numero <- function(numero) {
  regex <- "^[A-Z0-9]{7}$"
  if (grepl (regex, numero)) {
    return(TRUE)
  }
  else {
    return(FALSE)
  }
}



################################################################################
################################################################################
######################FONCTION NOM ET PRENOM VALIDE ############################

nom_prenom_valide <- function(prenom, parametre)
{
  if (is.na(prenom) || prenom == "") {
    return (FALSE)
  }
  else{
    if (nchar(prenom) >= parametre) {
      for (i in c(1:nchar(prenom))) {
        if (substring(prenom, i, i) %in% c(0:9)) {
          return(FALSE)
        }
      }
      return(TRUE)
    } else {
      return(FALSE)
    }
    
  }
}


################################################################################
################################################################################
#################SUPPRIMER LES ESPACES UNITULES SUR UNE CHAINE##################

supprime_espace_inutile <- function(date) {
  if (is.na(date) || date == "") {
    return(date)
  } else {
    date_sans_espace <- ""
    if (substring(date, 1, 1) != " ") {
      date_sans_espace <- paste0(date_sans_espace, substring(date, 1, 1))
    }
    for (i in c(2:nchar(date))) {
      if (!(substring(date, i - 1, i - 1) == " " &&
            substring(date, i, i) == " ")) {
        date_sans_espace <- paste0(date_sans_espace, substring(date, i, i))
      }
    }
  }
  return(date_sans_espace)
}

################################################################################
################################################################################
###############TRASFORMONS TOUTES LES SEPARATEUR EN TIRET(-)####################

transformation_des_separateurs_en_tiret <- function(date) {
  date1 <- ""
  for (i in 1:nchar(date)) {
    if (substring(date, i, i) %in% c("|", ",", ";", ":", " ", "/", ".", "_")) {
      date1 <- paste0(date1, "-")
    } else {
      date1 <- paste0(date1, substring(date, i, i))
    }
  }
  return(date1)
}



################################################################################
################################################################################
##################CHANGEONS LE FORMAT DE LA DATE ###############################


Sys.setlocale("LC_TIME", "fr_FR.UTF-8")

changer_format_de_la_date <- function(date) {
  if (is.na(date) || date == "") {
    return(date)
  } else {
    date <- gsub("janvier", "01", date, ignore.case = TRUE)
    date <- gsub("février", "02", date, ignore.case = TRUE)
    date <- gsub("mars", "03", date, ignore.case = TRUE)
    date <- gsub("avril", "04", date, ignore.case = TRUE)
    date <- gsub("mai", "05", date, ignore.case = TRUE)
    date <- gsub("juin", "06", date, ignore.case = TRUE)
    date <- gsub("juillet", "07", date, ignore.case = TRUE)
    date <- gsub("août", "08", date, ignore.case = TRUE)
    date <- gsub("septembre", "09", date, ignore.case = TRUE)
    date <- gsub("octobre", "10", date, ignore.case = TRUE)
    date <- gsub("novembre", "11", date, ignore.case = TRUE)
    date <- gsub("décembre", "12", date, ignore.case = TRUE)
    date <- gsub("decembre", "12", date, ignore.case = TRUE)
    date <- gsub("fev", "02", date, ignore.case = TRUE)

    formats <- c("%d-%B-%Y", "%d-%B-%y", "%d-%m-%Y", "%d-%m-%y")
    for (format_date in formats) {
      date1 <- as.Date(date, format_date)
      if (!is.na(date1)) {
        nouveau_date <- format(date1, "%d-%m-%y")
        return(nouveau_date)
      }
    }
    return(date) 
  }
}

#####################################################################################
#################################################################################
########################


est_date_valide <- function(date) {
  date <- as.Date(date, format = "%d-%m-%y")
  if (is.na(date)) {
    return(FALSE)
  }
  else{
    return(TRUE)
  }
}

#################################################################################
######################################################################################
################## CHANGEONS LE FORMAT D'ECRITURE DES CLASSE ####################


changer_format_classe <- function(classe) {
  format_classe <- ""
  for (i in 1:nchar(classe)) {
    if (substr(classe, i, i) %in% c('3', '4', '5', '6', 'A', 'B')) {
      format_classe <-
        paste(format_classe, substr(classe, i, i), sep = "")
    }
  }
  return(format_classe)
}

################################################################################
################################################################################
################### VERIFIONS SI LA DATE EST EST VALIDE ########################
is_valid_classe <- function(classe) {
  if (nchar(classe) != 2) {
    return(FALSE)
  }
  if (!grepl("^[3-6]$", substr(classe, 1, 1))) {
    return(FALSE)
  }
  if (!grepl("^[AB]$", substr(classe, 2, 2))) {
    return(FALSE)
  }
  return(TRUE)
}


#################################################################################
#################################################################################
#####################  changer le format des notes


changer_format_note = function(note) {
  if (is.na(note) || note == "") {
    return(note)
  } else{
    notes = list()
    
    note = gsub("Science_Physique", "PC", note, ignore.case = TRUE)
    note = gsub("Pc", "PC", note, ignore.case = TRUE)
    note = gsub("pc", "PC", note, ignore.case = TRUE)
    note = gsub("MATH", "Math", note, ignore.case = TRUE)
    note = gsub("ANGLAIS", "Anglais", note, ignore.case = TRUE)
    note = gsub("FRANCAIS", "Francais", note, ignore.case = TRUE)
    note = gsub("Français", "Francais", note, ignore.case = TRUE)
    note = gsub(" ", "", note, ignore.case = TRUE)
    
    note <- strsplit(note, "#")[[1]]
    note = note[nchar(note) != 0]
    
    matiere_et_note = c()
    
    note_finale = list()
    for (i in 1:length(note)) {
      matiere_et_note = strsplit(note[i], "\\[")[[1]]
      
      matiere = paste0(matiere_et_note[1], ":")
      note_de_la_matiere = matiere_et_note[-1]
      
      devoir_exam = strsplit(note_de_la_matiere, "\\:")[[1]]
      devoir_exam
      devoir = strsplit(devoir_exam[1], "\\|")[[1]]
      toute_les_notes = c("devoir:", devoir, "exam:", devoir_exam[-1])
      
      toute_les_notes = gsub("]", "", toute_les_notes, ignore.case = TRUE)
      toute_les_notes = gsub(",", ".", toute_les_notes, ignore.case = TRUE)
      toute_les_not = as.character(toute_les_notes)
      
      note_finale = c(note_finale, matiere, toute_les_not)
      note_fina = as.character(note_finale)
      
    }
    return(note_fina)
  }
}

#################################################################################
#################################################################################
#######################


est_note_valide = function(note) {
  if (is.na(note) || note == "") {
    return(FALSE)
  }
  else{
    for (i in c(1:length(note))) {
      if (!(
        note[i] %in% c(
          "PC:",
          "SVT:",
          "HG:",
          "Francais:",
          "Anglais:",
          "Math:",
          "devoir:",
          "exam:"
        )
      )) {
        if (is.na(as.numeric(note[i]))  ||
            !(as.numeric(note[i]) >= 0 &&
              as.numeric(note[i]) <= 20)) {
          return(FALSE)
        }
      }
    }
    return(TRUE)
  }
}


################################################################################
################################################################################
#####################

separation_des_donnees_en_valide_et_invalide = function(donnecsv) {
  donne_valide = data.frame(
    Code = character(),
    Numero = numeric(),
    Nom = character(),
    Prenom = character(),
    Date.de.naissance = character(),
    Classe = character(),
    Note = character()
  )
  
  donne_invalide = data.frame(
    Code = character(),
    Numero = numeric(),
    Nom = character(),
    Prenom = character(),
    Date.de.naissance = character(),
    Classe = character(),
    Note = character()
  )
  
  
  for (i in c(1:220)) {
    cmpt = 0
    
    if (is_valid_numero(donnecsv[i, 2]) == TRUE) {
      cmpt = cmpt + 1
    } else {
      donnecsv[i, 2] = paste0(donnecsv[i, 2], "⚠️")
      
    }
    if (nom_prenom_valide(donnecsv[i, 3], parametre = 2) == TRUE) {
      cmpt = cmpt + 1
    } else{
      donnecsv[i, 3] = paste0(donnecsv[i, 3], "⚠")
    }
    
    if (nom_prenom_valide(donnecsv[i, 4], parametre = 3) == TRUE) {
      cmpt = cmpt + 1
    } else{
      donnecsv[i, 4] = paste0(donnecsv[i, 4], "⚠")
    }
    
    date = supprime_espace_inutile(donnecsv[i, 5])
    date1 = transformation_des_separateurs_en_tiret(date)
    date2 = changer_format_de_la_date(date1)
    if (est_date_valide(date2) == TRUE) {
      cmpt = cmpt + 1
    } else{
      donnecsv[i, 5] = paste0(date2, "⚠")
    }
    
    classe = changer_format_classe(donnecsv[i, 6])
    if (is_valid_classe(classe) == TRUE) {
      cmpt = cmpt + 1
    } else{
      donnecsv[i, 6] = paste0(donnecsv[i, 6], "⚠")
    }
    
    note = changer_format_note(donnecsv[i, 7])
    if (est_note_valide(note) == TRUE) {
      cmpt = cmpt + 1
    } else{
      donnecsv[i, 7] = paste0(donnecsv[i, 7], "⚠")
    }

    if (cmpt == 6) {
      donne_valide = rbind(donne_valide, c(
        donnecsv[i, 1],
        donnecsv[i, 2],
        donnecsv[i, 3],
        donnecsv[i, 4],
        donnecsv[i, 5],
        donnecsv[i, 6],
        donnecsv[i, 7]
      ))
    } else{
      donne_invalide = rbind(
        donne_invalide,
        c(
          donnecsv[i, 1],
          donnecsv[i, 2],
          donnecsv[i, 3],
          donnecsv[i, 4],
          donnecsv[i, 5],
          donnecsv[i, 6],
          donnecsv[i, 7]
        )
      )
    }
  }
  
  donne = list(donne_valide, donne_invalide)
  return(donne)
}

