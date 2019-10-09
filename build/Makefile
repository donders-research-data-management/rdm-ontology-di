#define the baseURL of the static content
ifndef BASEURL
BASEURL=/doc
endif

#files to be included in the distribution
DUA=$(wildcard ../doc/dua/*)
LOGOS=$(wildcard ../doc/style/logo*.png)
BACKGROUND=../doc/style/background.jpg
BADGES=$(wildcard ../doc/style/badge*.svg)
BUILDINFO=build.txt
COLL_KEYWORDS=$(patsubst %.csv,%.json,$(wildcard ../doc/keyword/*.csv))
VOC_ETHICAL_REVIEW_BOARD=../doc/ethics/ethics_review_board.json
VOC_PUBLICATION_SYSTEM=$(wildcard ../doc/publication/*publication_system.json)
CMS_EXT_RSRC_IDX=external_urls.json
CMS_SNIPPETS_MD=$(patsubst %.md,%.html,$(wildcard doc/privacy/*.md))
CMS_SNIPPETS_HTML=$(wildcard ../doc/privacy/*.html ../doc/*.html ../doc/email/*.html ../doc/messages/*.html ../doc/changestate/*.html ../doc/login/*.html ../doc/editcollection/*.html ../doc/collection/*.html ../doc/collection/publish/*.html ../doc/collection/archive/*.html)
COLL_README_TXT=../doc/collection/publish/README.txt

#the directory containing help documentations in RST format
DIR_HELPDOC=../doc/help
DIR_HELPDOC_HTML=_build/$(notdir $(DIR_HELPDOC))
TMPDIR := $(shell mktemp -d)

#list of JSON files subject for validation
JSON_FILES=$(wildcard ../doc/dua/*.json) $(VOC_ETHICAL_REVIEW_BOARD) $(VOC_PUBLICATION_SYSTEM) $(CMS_EXT_RSRC_IDX) $(COLL_KEYWORDS)

JSON_SCHEMAS=$(wildcard $(patsubst %.json,%.schema,$(JSON_FILES)))

#list of files to be included in distribution or installation
DIST_FILES=$(DUA) $(LOGOS) $(BACKGROUND) $(BADGES) $(COLL_KEYWORDS) $(VOC_ETHICAL_REVIEW_BOARD) $(VOC_PUBLICATION_SYSTEM) $(CMS_SNIPPETS_MD) $(CMS_SNIPPETS_HTML) $(COLL_README_TXT)

#constant
VERSION:=master
INSTALL_PREFIX:=/tmp/rdm-ontology
DIST_ZIP:=rdm-configurable-content-$(VERSION).tar.gz

#targets
.PHONY: build dist install $(BUILDINFO) $(JSON_SCHEMAS) $(CMS_EXT_RSRC_IDX)

# convert contents into proper formats
build: $(COLL_KEYWORDS) $(CMS_SNIPPETS_MD) $(BUILDINFO) $(DIR_HELPDOC_HTML)

help: $(DIR_HELPDOC_HTML)

$(COLL_KEYWORDS):
	@echo "--> converting keyword: $@"
	python "$(shell pwd)/tools/csv2json.py" "$(patsubst %.json,%.csv,$@)" "$@"

$(CMS_SNIPPETS_MD):
	@echo "--> converting HTML snippet: $@"
	@python "$(shell pwd)/tools/md2html.py" "$(patsubst %.html,%.md,$@)"

$(CMS_EXT_RSRC_IDX):
	@echo "--> build index file: $@"
	sed "s|http://data.donders.ru.nl|$(BASEURL)|g" ../$(CMS_EXT_RSRC_IDX) > $(CMS_EXT_RSRC_IDX).tmp

$(DIR_HELPDOC_HTML):
	@echo "--> build helpdoc files in $(DIR_HELPDOC)"
	cp -R $(DIR_HELPDOC)/* $(TMPDIR) && \
		if [ -d $(TMPDIR)/_build ]; then rm -rf $(TMPDIR)/_build; fi && \
		ls -l $(TMPDIR) && \
		rm -f $(TMPDIR)/conf.py && \
		cp -R $(shell pwd)/tools/sphinx/* $(TMPDIR) && \
		make -C $(TMPDIR) html
	find $(TMPDIR)/_build/html -name '*.html' -exec \
		sed -i'' 's|.*src="_static/jquery.js".*||g' {} +
	mkdir -p $@ && mv $(TMPDIR)/_build/html/* $@
	rm -rf $(TMPDIR)

# validate JSON file when the corresponding .schema file is presented
validate_json: $(JSON_SCHEMAS)

$(JSON_SCHEMAS):
	@echo "--> validating JSON document: $(patsubst %.schema,%.json,$@)"
	@python "$(shell pwd)/tools/json-validator.py" "$(patsubst %.schema,%.json,$@)" "$@"

# make distribution tarball
dist: $(DIST_ZIP)
	@echo "--> checking resource availability ..."
	@python "$(shell pwd)/tools/check-external-urls.py" -p $(BASEURL) -l 3 -i $(CMS_EXT_RSRC_IDX) $(DIST_ZIP)

$(BUILDINFO):
	@if [ -f $@ ]; then cp $@ $@.dist; else touch $@.dist; fi

$(DIST_ZIP): build validate_json $(CMS_EXT_RSRC_IDX)
	@echo "--> packing $(DIST_ZIP) ..."
	@if [ ! -d dist ]; then mkdir dist; fi 
	@$(foreach d,$(dir $(DIST_FILES)),mkdir -p $(patsubst ../doc/%,dist/%,$(d));)
	@$(foreach f,$(DIST_FILES),cp $(f) $(patsubst ../doc/%,dist/%,$(f));)
	@cp $(BUILDINFO).dist dist/$(BUILDINFO)
	@mv $(CMS_EXT_RSRC_IDX).tmp dist/$(CMS_EXT_RSRC_IDX)
	@mkdir -p dist/help && cp -R $(DIR_HELPDOC_HTML)/* dist/help
	@cd dist && COPYFILE_DISABLE=true tar cvzf ../$@ * && cd -

# install
install: build validate_json $(CMS_EXT_RSRC_IDX)
	$(foreach d,$(dir $(DIST_FILES)),install -d -m 0755 $(INSTALL_PREFIX)/$(d);)
	$(foreach f,$(DIST_FILES),install -m 0644 $(f) $(INSTALL_PREFIX)/$(f);)
	@install -m 0644 $(CMS_EXT_RSRC_IDX).tmp $(INSTALL_PREFIX)/$(CMS_EXT_RSRC_IDX)

# clean 
clean:
	@if [ -f $(DIST_ZIP) ]; then rm -f $(DIST_ZIP); fi
	$(foreach f,$(COLL_KEYWORDS),rm -f $(f);)
	$(foreach f,$(CMS_SNIPPETS_MD),rm -f $(f);)
	@if [ -f $(CMS_EXT_RSRC_IDX).tmp ]; then rm $(CMS_EXT_RSRC_IDX).tmp; fi
	@if [ -d dist ]; then rm -rf dist; fi
	@if [ -f $(BUILDINFO).dist ]; then rm -rf $(BUILDINFO).dist; fi
	@if [ -d _build ]; then rm -rf _build; fi
