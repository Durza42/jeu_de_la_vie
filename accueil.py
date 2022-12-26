import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

SPACE_BETWEEN_WIDGETS = 20

def menu(params):

    def on_x_ok(button):
        params["nb_carres_x"] = button.get_value_as_int()

    def on_y_ok(button):
        params["nb_carres_y"] = button.get_value_as_int()

    def on_attente_ok(button):
        params["attente"] = button.get_value_as_int()

    def on_path_ok(button):
        print("TODO: path")

    def launch_app(button):
        params["continue"] = True
        Gtk.main_quit()

    class LabelPlusTextEntry():
        def __init__(self, vbox, text:str, callback):
            self.horizontal_box = Gtk.Box()
            self.legende = Gtk.Label(label=text)
            self.entry = Gtk.Entry()
            self.ok = Gtk.Button.new_with_label(label="apply")
            self.ok.connect("clicked", callback)

            vbox.pack_start(self.horizontal_box, False, False, SPACE_BETWEEN_WIDGETS)

            self.horizontal_box.pack_start(self.legende, False, False, SPACE_BETWEEN_WIDGETS)
            self.horizontal_box.pack_start(self.entry, False, False, SPACE_BETWEEN_WIDGETS)
            self.horizontal_box.pack_start(self.ok, False, False, SPACE_BETWEEN_WIDGETS)

    class LabelPlusNumberEntry():
        def __init__(self, vbox, text:str, default:int, callback):
            self.horizontal_box = Gtk.Box()
            self.legende = Gtk.Label(label=text)

            adjustment = Gtk.Adjustment(upper=5000, step_increment=1, page_increment=10)
            self.getnumber = Gtk.SpinButton()
            self.getnumber.set_adjustment(adjustment)
            self.getnumber.connect("value-changed", callback)
            self.getnumber.set_numeric(True)
            self.getnumber.set_value(default)

            self.ok = Gtk.Button.new_with_label(label="Apply")

            vbox.pack_start(self.horizontal_box, False, False, SPACE_BETWEEN_WIDGETS)

            self.horizontal_box.pack_start(self.legende, False, False, SPACE_BETWEEN_WIDGETS)
            self.horizontal_box.pack_start(self.getnumber, False, False, SPACE_BETWEEN_WIDGETS)
            self.horizontal_box.pack_start(self.ok, False, False, SPACE_BETWEEN_WIDGETS)


    class MyWindow(Gtk.Window):
        def __init__(self):
            super().__init__(title="Accueil")
            self.set_border_width(40)

            self.titre = Gtk.Label(label="Le jeu de le vie")
            self.titre.set_markup("<span foreground=\"white\" size=\"xx-large\">  Bienvenue dans le jeu de la vie !  </span>")

            self.vertical_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
            self.add(self.vertical_box)

            self.vertical_box.pack_start(self.titre, False, False, SPACE_BETWEEN_WIDGETS)

            demande_taille_x = LabelPlusNumberEntry(self.vertical_box, "entrez la taille x :", 30, on_x_ok)
            demande_taille_y = LabelPlusNumberEntry(self.vertical_box, "entrez la taille y :", 20, on_y_ok)
            demande_attente  = LabelPlusNumberEntry(self.vertical_box, "l'attente entre deux frames (en ms) :", 300, on_attente_ok)

## pour l'instant
#            demande_chemin_sauvegarde = LabelPlusTextEntry(self.vertical_box, "ou entrez le chemin du fichier de sauvegarde :", on_path_ok)
##

            self.launch = Gtk.Button.new_with_label(label="lancer le jeu de la vie selon ces paramètres")
            self.launch.connect("clicked", launch_app)
            self.vertical_box.pack_start(self.launch, False, False, SPACE_BETWEEN_WIDGETS)


    window = MyWindow()
    window.connect("destroy", Gtk.main_quit)

    window.show_all()
    Gtk.main()
