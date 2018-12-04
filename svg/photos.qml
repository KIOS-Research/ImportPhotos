<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis minScale="1e+08" readOnly="0" simplifyLocal="1" labelsEnabled="0" styleCategories="AllStyleCategories" simplifyMaxScale="1" hasScaleBasedVisibilityFlag="0" maxScale="0" simplifyAlgorithm="0" simplifyDrawingHints="0" simplifyDrawingTol="1" version="3.4.2-Madeira">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <renderer-v2 forceraster="0" symbollevels="0" enableorderby="0" type="singleSymbol">
    <symbols>
      <symbol clip_to_extent="1" name="0" alpha="1" type="marker">
        <layer class="SimpleMarker" pass="0" locked="0" enabled="1">
          <prop v="0" k="angle"/>
          <prop v="97,97,97,255" k="color"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="square" k="name"/>
          <prop v="0.00000000000000006,-10" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="Pixel" k="offset_unit"/>
          <prop v="0,0,0,0" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0" k="outline_width"/>
          <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
          <prop v="Pixel" k="outline_width_unit"/>
          <prop v="diameter" k="scale_method"/>
          <prop v="5.4" k="size"/>
          <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
          <prop v="Pixel" k="size_unit"/>
          <prop v="1" k="vertical_anchor_point"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties" type="Map">
                <Option name="angle" type="Map">
                  <Option value="true" name="active" type="bool"/>
                  <Option value="if(TO_REAL( &quot;Azimuth&quot; )=0,'',TO_REAL( &quot;Azimuth&quot; ))" name="expression" type="QString"/>
                  <Option value="3" name="type" type="int"/>
                </Option>
                <Option name="size" type="Map">
                  <Option value="true" name="active" type="bool"/>
                  <Option value="if( &quot;AZIMUTH&quot; !=0,5.4,0)" name="expression" type="QString"/>
                  <Option value="3" name="type" type="int"/>
                </Option>
              </Option>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
        <layer class="SimpleMarker" pass="0" locked="0" enabled="1">
          <prop v="0" k="angle"/>
          <prop v="255,255,255,255" k="color"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="square" k="name"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="Pixel" k="offset_unit"/>
          <prop v="97,97,97,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0" k="outline_width"/>
          <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
          <prop v="Pixel" k="outline_width_unit"/>
          <prop v="diameter" k="scale_method"/>
          <prop v="14" k="size"/>
          <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
          <prop v="Pixel" k="size_unit"/>
          <prop v="1" k="vertical_anchor_point"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties" type="Map">
                <Option name="angle" type="Map">
                  <Option value="false" name="active" type="bool"/>
                  <Option value="if(TO_REAL( &quot;Azimuth&quot; )=0,'',TO_REAL( &quot;Azimuth&quot; ))" name="expression" type="QString"/>
                  <Option value="3" name="type" type="int"/>
                </Option>
              </Option>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
        <layer class="SimpleMarker" pass="0" locked="0" enabled="1">
          <prop v="0" k="angle"/>
          <prop v="97,97,97,255" k="color"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="triangle" k="name"/>
          <prop v="-2,1" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="Pixel" k="offset_unit"/>
          <prop v="0,0,0,0" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0" k="outline_width"/>
          <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
          <prop v="Pixel" k="outline_width_unit"/>
          <prop v="diameter" k="scale_method"/>
          <prop v="5" k="size"/>
          <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
          <prop v="Pixel" k="size_unit"/>
          <prop v="1" k="vertical_anchor_point"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties" type="Map">
                <Option name="angle" type="Map">
                  <Option value="false" name="active" type="bool"/>
                  <Option value="if(TO_REAL( &quot;Azimuth&quot; )=0,'',TO_REAL( &quot;Azimuth&quot; ))" name="expression" type="QString"/>
                  <Option value="3" name="type" type="int"/>
                </Option>
              </Option>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
        <layer class="SimpleMarker" pass="0" locked="0" enabled="1">
          <prop v="0" k="angle"/>
          <prop v="97,97,97,255" k="color"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="triangle" k="name"/>
          <prop v="2,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="Pixel" k="offset_unit"/>
          <prop v="0,0,0,0" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0" k="outline_width"/>
          <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
          <prop v="Pixel" k="outline_width_unit"/>
          <prop v="diameter" k="scale_method"/>
          <prop v="7" k="size"/>
          <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
          <prop v="Pixel" k="size_unit"/>
          <prop v="1" k="vertical_anchor_point"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties" type="Map">
                <Option name="angle" type="Map">
                  <Option value="false" name="active" type="bool"/>
                  <Option value="if(TO_REAL( &quot;Azimuth&quot; )=0,'',TO_REAL( &quot;Azimuth&quot; ))" name="expression" type="QString"/>
                  <Option value="3" name="type" type="int"/>
                </Option>
              </Option>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
        <layer class="SimpleMarker" pass="0" locked="0" enabled="1">
          <prop v="0" k="angle"/>
          <prop v="97,97,97,255" k="color"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="square" k="name"/>
          <prop v="-1,-3" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="Pixel" k="offset_unit"/>
          <prop v="0,0,0,0" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0" k="outline_width"/>
          <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
          <prop v="Pixel" k="outline_width_unit"/>
          <prop v="diameter" k="scale_method"/>
          <prop v="2" k="size"/>
          <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
          <prop v="Pixel" k="size_unit"/>
          <prop v="1" k="vertical_anchor_point"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties" type="Map">
                <Option name="angle" type="Map">
                  <Option value="false" name="active" type="bool"/>
                  <Option value="if(TO_REAL( &quot;Azimuth&quot; )=0,'',TO_REAL( &quot;Azimuth&quot; ))" name="expression" type="QString"/>
                  <Option value="3" name="type" type="int"/>
                </Option>
                <Option name="size" type="Map">
                  <Option value="false" name="active" type="bool"/>
                  <Option value="if( &quot;AZIMUTH&quot; !=0,2,0)" name="expression" type="QString"/>
                  <Option value="3" name="type" type="int"/>
                </Option>
              </Option>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
    </symbols>
    <rotation/>
    <sizescale/>
  </renderer-v2>
  <customproperties>
    <property value="ID" key="dualview/previewExpressions"/>
    <property value="0" key="embeddedWidgets/count"/>
    <property key="variableNames"/>
    <property key="variableValues"/>
  </customproperties>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerOpacity>1</layerOpacity>
  <SingleCategoryDiagramRenderer attributeLegend="1" diagramType="Histogram">
    <DiagramCategory penAlpha="255" labelPlacementMethod="XHeight" penWidth="0" minimumSize="0" minScaleDenominator="0" barWidth="5" diagramOrientation="Up" lineSizeScale="3x:0,0,0,0,0,0" enabled="0" sizeType="MM" height="15" scaleBasedVisibility="0" penColor="#000000" sizeScale="3x:0,0,0,0,0,0" backgroundAlpha="255" rotationOffset="270" lineSizeType="MM" backgroundColor="#ffffff" maxScaleDenominator="1e+08" opacity="1" width="15" scaleDependency="Area">
      <fontProperties description="MS Shell Dlg 2,8.25,-1,5,50,0,0,0,0,0" style=""/>
      <attribute label="" field="" color="#000000"/>
    </DiagramCategory>
  </SingleCategoryDiagramRenderer>
  <DiagramLayerSettings dist="0" obstacle="0" zIndex="0" showAll="1" placement="0" priority="0" linePlacementFlags="18">
    <properties>
      <Option type="Map">
        <Option value="" name="name" type="QString"/>
        <Option name="properties"/>
        <Option value="collection" name="type" type="QString"/>
      </Option>
    </properties>
  </DiagramLayerSettings>
  <geometryOptions geometryPrecision="0" removeDuplicateNodes="0">
    <activeChecks/>
    <checkConfiguration/>
  </geometryOptions>
  <fieldConfiguration>
    <field name="ID">
      <editWidget type="Hidden">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="Name">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="Date">
      <editWidget type="DateTime">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="Time">
      <editWidget type="DateTime">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="Lon">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="Lat">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="Altitude">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="North">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="Azimuth">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="Camera Maker">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="Camera Model">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="Path">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
  </fieldConfiguration>
  <aliases>
    <alias field="ID" index="0" name=""/>
    <alias field="Name" index="1" name=""/>
    <alias field="Date" index="2" name=""/>
    <alias field="Time" index="3" name=""/>
    <alias field="Lon" index="4" name=""/>
    <alias field="Lat" index="5" name=""/>
    <alias field="Altitude" index="6" name=""/>
    <alias field="North" index="7" name=""/>
    <alias field="Azimuth" index="8" name=""/>
    <alias field="Camera Maker" index="9" name=""/>
    <alias field="Camera Model" index="10" name=""/>
    <alias field="Path" index="11" name=""/>
  </aliases>
  <excludeAttributesWMS/>
  <excludeAttributesWFS/>
  <defaults>
    <default field="ID" expression="" applyOnUpdate="0"/>
    <default field="Name" expression="" applyOnUpdate="0"/>
    <default field="Date" expression="" applyOnUpdate="0"/>
    <default field="Time" expression="" applyOnUpdate="0"/>
    <default field="Lon" expression="" applyOnUpdate="0"/>
    <default field="Lat" expression="" applyOnUpdate="0"/>
    <default field="Altitude" expression="" applyOnUpdate="0"/>
    <default field="North" expression="" applyOnUpdate="0"/>
    <default field="Azimuth" expression="" applyOnUpdate="0"/>
    <default field="Camera Maker" expression="" applyOnUpdate="0"/>
    <default field="Camera Model" expression="" applyOnUpdate="0"/>
    <default field="Path" expression="" applyOnUpdate="0"/>
  </defaults>
  <constraints>
    <constraint constraints="0" notnull_strength="0" field="ID" unique_strength="0" exp_strength="0"/>
    <constraint constraints="0" notnull_strength="0" field="Name" unique_strength="0" exp_strength="0"/>
    <constraint constraints="0" notnull_strength="0" field="Date" unique_strength="0" exp_strength="0"/>
    <constraint constraints="0" notnull_strength="0" field="Time" unique_strength="0" exp_strength="0"/>
    <constraint constraints="0" notnull_strength="0" field="Lon" unique_strength="0" exp_strength="0"/>
    <constraint constraints="0" notnull_strength="0" field="Lat" unique_strength="0" exp_strength="0"/>
    <constraint constraints="0" notnull_strength="0" field="Altitude" unique_strength="0" exp_strength="0"/>
    <constraint constraints="0" notnull_strength="0" field="North" unique_strength="0" exp_strength="0"/>
    <constraint constraints="0" notnull_strength="0" field="Azimuth" unique_strength="0" exp_strength="0"/>
    <constraint constraints="0" notnull_strength="0" field="Camera Maker" unique_strength="0" exp_strength="0"/>
    <constraint constraints="0" notnull_strength="0" field="Camera Model" unique_strength="0" exp_strength="0"/>
    <constraint constraints="0" notnull_strength="0" field="Path" unique_strength="0" exp_strength="0"/>
  </constraints>
  <constraintExpressions>
    <constraint field="ID" exp="" desc=""/>
    <constraint field="Name" exp="" desc=""/>
    <constraint field="Date" exp="" desc=""/>
    <constraint field="Time" exp="" desc=""/>
    <constraint field="Lon" exp="" desc=""/>
    <constraint field="Lat" exp="" desc=""/>
    <constraint field="Altitude" exp="" desc=""/>
    <constraint field="North" exp="" desc=""/>
    <constraint field="Azimuth" exp="" desc=""/>
    <constraint field="Camera Maker" exp="" desc=""/>
    <constraint field="Camera Model" exp="" desc=""/>
    <constraint field="Path" exp="" desc=""/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction value="{00000000-0000-0000-0000-000000000000}" key="Canvas"/>
  </attributeactions>
  <attributetableconfig sortOrder="1" sortExpression="&quot;Camera Model&quot;" actionWidgetStyle="dropDown">
    <columns>
      <column hidden="0" width="-1" name="ID" type="field"/>
      <column hidden="1" width="-1" type="actions"/>
      <column hidden="0" width="-1" name="Name" type="field"/>
      <column hidden="0" width="-1" name="Date" type="field"/>
      <column hidden="0" width="-1" name="Time" type="field"/>
      <column hidden="0" width="-1" name="Lon" type="field"/>
      <column hidden="0" width="-1" name="Lat" type="field"/>
      <column hidden="0" width="-1" name="Altitude" type="field"/>
      <column hidden="0" width="-1" name="North" type="field"/>
      <column hidden="0" width="-1" name="Azimuth" type="field"/>
      <column hidden="0" width="-1" name="Camera Maker" type="field"/>
      <column hidden="0" width="-1" name="Camera Model" type="field"/>
      <column hidden="0" width="-1" name="Path" type="field"/>
    </columns>
  </attributetableconfig>
  <conditionalstyles>
    <rowstyles/>
    <fieldstyles/>
  </conditionalstyles>
  <editform tolerant="1"></editform>
  <editforminit/>
  <editforminitcodesource>0</editforminitcodesource>
  <editforminitfilepath></editforminitfilepath>
  <editforminitcode><![CDATA[# -*- coding: utf-8 -*-
"""
QGIS forms can have a Python function that is called when the form is
opened.

Use this function to add extra logic to your forms.

Enter the name of the function in the "Python Init function"
field.
An example follows:
"""
from qgis.PyQt.QtWidgets import QWidget

def my_form_open(dialog, layer, feature):
	geom = feature.geometry()
	control = dialog.findChild(QWidget, "MyLineEdit")
]]></editforminitcode>
  <featformsuppress>0</featformsuppress>
  <editorlayout>generatedlayout</editorlayout>
  <editable>
    <field editable="1" name="ALTITUDE"/>
    <field editable="1" name="AZIMUTH"/>
    <field editable="1" name="Altitude"/>
    <field editable="1" name="Azimuth"/>
    <field editable="1" name="CAMERA MAK"/>
    <field editable="1" name="CAMERA MOD"/>
    <field editable="1" name="Camera Maker"/>
    <field editable="1" name="Camera Model"/>
    <field editable="1" name="DATE"/>
    <field editable="1" name="Date"/>
    <field editable="1" name="ID"/>
    <field editable="1" name="LAT"/>
    <field editable="1" name="LON"/>
    <field editable="1" name="Lat"/>
    <field editable="1" name="Lon"/>
    <field editable="1" name="NAME"/>
    <field editable="1" name="NORTH"/>
    <field editable="1" name="Name"/>
    <field editable="1" name="North"/>
    <field editable="1" name="PATH"/>
    <field editable="1" name="Path"/>
    <field editable="1" name="TIME"/>
    <field editable="1" name="Time"/>
  </editable>
  <labelOnTop>
    <field name="ALTITUDE" labelOnTop="0"/>
    <field name="AZIMUTH" labelOnTop="0"/>
    <field name="Altitude" labelOnTop="0"/>
    <field name="Azimuth" labelOnTop="0"/>
    <field name="CAMERA MAK" labelOnTop="0"/>
    <field name="CAMERA MOD" labelOnTop="0"/>
    <field name="Camera Maker" labelOnTop="0"/>
    <field name="Camera Model" labelOnTop="0"/>
    <field name="DATE" labelOnTop="0"/>
    <field name="Date" labelOnTop="0"/>
    <field name="ID" labelOnTop="0"/>
    <field name="LAT" labelOnTop="0"/>
    <field name="LON" labelOnTop="0"/>
    <field name="Lat" labelOnTop="0"/>
    <field name="Lon" labelOnTop="0"/>
    <field name="NAME" labelOnTop="0"/>
    <field name="NORTH" labelOnTop="0"/>
    <field name="Name" labelOnTop="0"/>
    <field name="North" labelOnTop="0"/>
    <field name="PATH" labelOnTop="0"/>
    <field name="Path" labelOnTop="0"/>
    <field name="TIME" labelOnTop="0"/>
    <field name="Time" labelOnTop="0"/>
  </labelOnTop>
  <widgets/>
  <previewExpression>ID</previewExpression>
  <mapTip></mapTip>
  <layerGeometryType>0</layerGeometryType>
</qgis>
